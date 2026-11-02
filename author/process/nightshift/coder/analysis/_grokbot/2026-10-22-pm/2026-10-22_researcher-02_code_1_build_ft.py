"""Build attempt-level NBA free-throw table with game context + workload.
Source: shufinskiy/nba_data (stats.nba.com play-by-play + shotdetail mirror), seasons 2015-16..2023-24.
"""
import pandas as pd, numpy as np, sys, re
D='../data/'
SEASONS=range(2015,2024)
COLS=['GAME_ID','EVENTNUM','EVENTMSGTYPE','EVENTMSGACTIONTYPE','PERIOD','PCTIMESTRING','HOMEDESCRIPTION','VISITORDESCRIPTION','SCORE','SCOREMARGIN',
      'PERSON1TYPE','PLAYER1_ID','PLAYER1_NAME','PLAYER1_TEAM_ID','PERSON2TYPE','PLAYER2_ID','PLAYER2_TEAM_ID','PERSON3TYPE','PLAYER3_ID','PLAYER3_TEAM_ID']
# FT action types: 10 1of1,11 1of2,12 2of2,13-15 1-3of3, 16 technical, 18/19 flagrant 1of2/2of2, 20 flagrant 1of1, 21/22 tech 1of2/2of2, 25/26 clear-path 1of2/2of2, 27-29 flagrant 1-3of3
TECH={16,21,22}
def clock(s):
    m,sec=s.split(':'); return int(m)*60+int(sec)
def elapsed(period,rem):
    base=np.where(period<=4,(period-1)*720,2880+(period-5)*300)
    plen=np.where(period<=4,720,300)
    return base+plen-rem

def minutes_by_game(pbp):
    """Approximate per-player seconds on court, cumulative within game, from subs + period-first-appearance."""
    rows=[]  # (game, player, team, period, start_el, end_el)
    for (g,p),ev in pbp.groupby(['GAME_ID','PERIOD'],sort=False):
        plen=720 if p<=4 else 300
        pstart=(p-1)*720 if p<=4 else 2880+(p-5)*300
        on={}; seen_in=set(); team={}
        ev=ev.sort_values(['EL','EVENTNUM'])
        for r in ev.itertuples(index=False):
            if r.EVENTMSGTYPE==8:
                out,inn=r.PLAYER1_ID,r.PLAYER2_ID
                team[out]=r.PLAYER1_TEAM_ID; team[inn]=r.PLAYER2_TEAM_ID
                if out not in seen_in and out not in on: on[out]=pstart  # starter of period
                if out in on: rows.append((g,out,team[out],p,on.pop(out),r.EL)); seen_in.add(out)
                else: seen_in.add(out)
                on[inn]=r.EL; seen_in.add(inn)
            else:
                for pid,pt,tid in ((r.PLAYER1_ID,r.PERSON1TYPE,r.PLAYER1_TEAM_ID),(r.PLAYER2_ID,r.PERSON2TYPE,r.PLAYER2_TEAM_ID),(r.PLAYER3_ID,r.PERSON3TYPE,r.PLAYER3_TEAM_ID)):
                    if pt in (4,5) and pid and pid not in seen_in and pid not in on:
                        on[pid]=pstart; team[pid]=tid; seen_in.add(pid)
        for pid,st in on.items(): rows.append((g,pid,team.get(pid),p,st,pstart+plen))
    return pd.DataFrame(rows,columns=['GAME_ID','PLAYER_ID','TEAM_ID','PERIOD','START','END'])

all_ft=[]; all_min=[]; sched=[]
for s in SEASONS:
    for st,fn in (('regular',f'nbastats_{s}.csv'),('playoffs',f'nbastats_po_{s}.csv')):
        pbp=pd.read_csv(D+fn,usecols=COLS,low_memory=False)
        pbp=pbp[pbp.PCTIMESTRING.notna()]
        pbp['REM']=pbp.PCTIMESTRING.map(clock); pbp['EL']=elapsed(pbp.PERIOD.values,pbp.REM.values)
        pbp=pbp.sort_values(['GAME_ID','EVENTNUM'])
        # running score: SCORE "AWAY - HOME" (verified: home basket increments 2nd number; SCOREMARGIN=home-away)
        sc=pbp.SCORE.str.extract(r'(\d+)\s*-\s*(\d+)').astype(float)
        pbp['AWAY_PTS']=sc[0]; pbp['HOME_PTS']=sc[1]
        pbp[['AWAY_PTS','HOME_PTS']]=pbp.groupby('GAME_ID')[['AWAY_PTS','HOME_PTS']].ffill().fillna(0)
        pbp['PRE_AWAY']=pbp.groupby('GAME_ID').AWAY_PTS.shift(1).fillna(0)
        pbp['PRE_HOME']=pbp.groupby('GAME_ID').HOME_PTS.shift(1).fillna(0)
        ft=pbp[pbp.EVENTMSGTYPE==3].copy()
        ft['IS_HOME']=ft.HOMEDESCRIPTION.notna()&ft.HOMEDESCRIPTION.str.contains('Free Throw',na=False)
        desc=np.where(ft.IS_HOME,ft.HOMEDESCRIPTION,ft.VISITORDESCRIPTION)
        ft['DESC']=desc
        ft=ft[pd.Series(desc,index=ft.index).fillna('').str.contains('Free Throw')]
        ft['MADE']=(~ft.DESC.str.startswith('MISS')).astype(int)
        ft['PRE_MARGIN']=np.where(ft.IS_HOME,ft.PRE_HOME-ft.PRE_AWAY,ft.PRE_AWAY-ft.PRE_HOME)
        ft['SEASON']=f'{s}-{str(s+1)[2:]}'; ft['SEASON_TYPE']=st
        ft['TECHNICAL']=ft.EVENTMSGACTIONTYPE.isin(TECH).astype(int)
        mins=minutes_by_game(pbp); mins['SEASON']=ft['SEASON'].iloc[0]; mins['SEASON_TYPE']=st
        all_ft.append(ft[['GAME_ID','EVENTNUM','SEASON','SEASON_TYPE','PERIOD','REM','EL','PLAYER1_ID','PLAYER1_NAME','PLAYER1_TEAM_ID','IS_HOME','EVENTMSGACTIONTYPE','TECHNICAL','PRE_MARGIN','MADE']])
        all_min.append(mins)
        sd=pd.read_csv(D+fn.replace('nbastats','shotdetail'),usecols=['GAME_ID','TEAM_ID','GAME_DATE'])
        sched.append(sd.drop_duplicates(['GAME_ID','TEAM_ID']))
        print(s,st,len(ft),mins.GAME_ID.nunique(),file=sys.stderr)
ft=pd.concat(all_ft); mins=pd.concat(all_min); sched=pd.concat(sched).drop_duplicates(['GAME_ID','TEAM_ID'])
ft.to_parquet('ft_raw.parquet'); mins.to_parquet('minutes_intervals.parquet'); sched.to_parquet('sched.parquet')
print('done',len(ft),file=sys.stderr)

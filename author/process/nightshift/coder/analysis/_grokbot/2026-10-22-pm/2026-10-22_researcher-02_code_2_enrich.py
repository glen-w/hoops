import pandas as pd, numpy as np
ft=pd.read_parquet('ft_raw.parquet'); mi=pd.read_parquet('minutes_intervals.parquet'); sc=pd.read_parquet('sched.parquet')
mi['SECS']=(mi.END-mi.START).clip(lower=0)
pg=mi.groupby(['GAME_ID','PLAYER_ID','TEAM_ID','SEASON','SEASON_TYPE'],as_index=False).SECS.sum()
pg['MIN']=pg.SECS/60
# validation: team minutes per game
tg=pg.groupby(['GAME_ID','TEAM_ID']).MIN.sum()
print('team-min per game: median',tg.median(),'p5',tg.quantile(.05),'p95',tg.quantile(.95))
sc['DATE']=pd.to_datetime(sc.GAME_DATE.astype(str))
sc=sc.drop_duplicates(['GAME_ID','TEAM_ID'])
pg=pg.merge(sc[['GAME_ID','TEAM_ID','DATE']],on=['GAME_ID','TEAM_ID'],how='left')
print('missing dates',pg.DATE.isna().mean())
# team schedule b2b (rest days) incl. both rg & po, within season
ts=sc.copy(); ts['SEASON_KEY']=ts.GAME_ID.astype(str).str[1:3]
ts=ts.sort_values(['TEAM_ID','DATE'])
ts['PREV']=ts.groupby(['TEAM_ID','SEASON_KEY']).DATE.shift(1)
ts['REST_DAYS']=(ts.DATE-ts.PREV).dt.days-1
ts['B2B']=(ts.REST_DAYS==0).astype(int)
# player workload: cumulative season minutes/games before game (regular+playoffs chained), minutes in prior 7 days
pg['SEASON_KEY']=pg.GAME_ID.astype(str).str[1:3]
pg=pg.sort_values(['PLAYER_ID','DATE','GAME_ID'])
g=pg.groupby(['PLAYER_ID','SEASON'])
pg['CUM_MIN_BEFORE']=g.MIN.cumsum()-pg.MIN
pg['GAMES_BEFORE']=g.cumcount()
def last7(df):
    s=df.set_index('DATE').MIN
    r=s.rolling('7D',closed='left').sum()
    return pd.Series(r.values,index=df.index)
pg['MIN_PRIOR_7D']=pg.groupby('PLAYER_ID',group_keys=False).apply(last7).fillna(0)
# season-end minutes per player (regular season) for seasonal workload level
sm=pg[pg.SEASON_TYPE=='regular'].groupby(['PLAYER_ID','SEASON']).agg(SEASON_MIN=('MIN','sum'),SEASON_GP=('GAME_ID','nunique')).reset_index()
pg.to_parquet('player_games.parquet'); sm.to_parquet('player_season_min.parquet')
# FT enrichment
ft=ft.rename(columns={'PLAYER1_ID':'PLAYER_ID','PLAYER1_NAME':'PLAYER_NAME','PLAYER1_TEAM_ID':'TEAM_ID'})
ft['TEAM_ID']=ft.TEAM_ID.astype('Int64'); pg['TEAM_ID']=pg.TEAM_ID.astype('Int64'); ts['TEAM_ID']=ts.TEAM_ID.astype('Int64')
ft=ft.merge(pg[['GAME_ID','PLAYER_ID','MIN','DATE','CUM_MIN_BEFORE','GAMES_BEFORE','MIN_PRIOR_7D']],on=['GAME_ID','PLAYER_ID'],how='left')
ft=ft.merge(ts[['GAME_ID','TEAM_ID','REST_DAYS','B2B']],on=['GAME_ID','TEAM_ID'],how='left')
# in-game seconds on court before this FT
iv=mi[['GAME_ID','PLAYER_ID','START','END']]
tmp=ft[['GAME_ID','PLAYER_ID','EL']].reset_index().merge(iv,on=['GAME_ID','PLAYER_ID'],how='left')
tmp['ON']=(np.minimum(tmp.END,tmp.EL)-tmp.START).clip(lower=0)
ft['INGAME_MIN_BEFORE']=(tmp.groupby('index').ON.sum()/60).reindex(ft.index).values
ft['ABS_MARGIN']=ft.PRE_MARGIN.abs()
ft['CLUTCH']=((ft.PERIOD>=4)&(ft.REM<=300)&(ft.ABS_MARGIN<=5)).astype(int)
ft['LATE_CLOSE']=((ft.PERIOD>=4)&(ft.REM<=60)&(ft.ABS_MARGIN<=3)).astype(int)
ft['LOW_PRESSURE']=((ft.PERIOD<=3)|(ft.ABS_MARGIN>=20)).astype(int)&(1-ft.CLUTCH)
ft['PLAYOFF']=(ft.SEASON_TYPE=='playoffs').astype(int)
ft['SECOND_OF_PAIR']=ft.EVENTMSGACTIONTYPE.isin([12,14,19,22,26]).astype(int)
ft['LAST_OF_TRIP']=ft.EVENTMSGACTIONTYPE.isin([10,12,15,19,20,22,26,29]).astype(int)
ft=ft.merge(sm,on=['PLAYER_ID','SEASON'],how='left')
ft.to_parquet('ft_enriched.parquet')
print(len(ft), ft[['MIN','DATE','B2B','INGAME_MIN_BEFORE','SEASON_MIN']].isna().mean().to_dict())
print(ft.groupby('SEASON').agg(n=('MADE','size'),pct=('MADE','mean')))

import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
ft=pd.read_parquet('ft_analysis.parquet')
base='MADE ~ BASE_LOGIT + SECOND_OF_PAIR + TECHNICAL + C(SEASON) + LATE_CLOSE + CLUTCH + PLAYOFF + B2B + INGAME_10 + CUM_MIN_500 + MIN7D_30 + HIGH_WL'
out=[]
def fit(name,f,df):
    m=smf.glm(f,data=df,family=sm.families.Binomial()).fit(cov_type='cluster',cov_kwds={'groups':df.PLAYER_ID.astype('int64')})
    pr=m.predict(df); sc=(pr*(1-pr)).mean(); ci=m.conf_int()
    for t in m.params.index:
        if t.startswith('C(SEASON)') or t=='Intercept': continue
        out.append(dict(model=name,term=t,coef_logodds=round(m.params[t],4),se_cluster_player=round(m.bse[t],4),ci95_low=round(ci.loc[t,0],4),ci95_high=round(ci.loc[t,1],4),p_value=round(m.pvalues[t],4),approx_ame_pp=round(100*sc*m.params[t],2),n=int(m.nobs),
          source='stats.nba.com PBP via shufinskiy/nba_data; logit with player-season leave-one-out FT% baseline; SE clustered by player',confidence='MEDIUM (observational; associations only)'))
    print(name,int(m.nobs))
fit('M4_lateclose_interactions',base+' + LATE_CLOSE:B2B + LATE_CLOSE:HIGH_WL + LATE_CLOSE:INGAME_10 + LATE_CLOSE:MIN7D_30',ft)
fit('M5_excl_2019-21_seasons',base,ft[~ft.SEASON.isin(['2019-20','2020-21'])])
fit('M6_trailing_vs_leading_lateclose',base+' + LATE_CLOSE:I(PRE_MARGIN<0)',ft)
prev=pd.read_csv('../out/2026-10-22_researcher-02_ft_models.csv')
pd.concat([prev,pd.DataFrame(out)]).to_csv('../out/2026-10-22_researcher-02_ft_models.csv',index=False)
d=pd.DataFrame(out); print(d[~d.term.isin(['BASE_LOGIT','SECOND_OF_PAIR','TECHNICAL'])][['model','term','coef_logodds','ci95_low','ci95_high','p_value','approx_ame_pp']].to_string())
# ---- player-season proxy table (for researcher-03)
ft['PRESS']=((ft.CLUTCH==1)|(ft.PLAYOFF==1)&(ft.PERIOD>=4)&(ft.ABS_MARGIN<=5)).astype(int)
ft['RESID']=ft.MADE-ft.BASE
ft=ft.sort_values(['PLAYER_ID','DATE','EL'])
def ps(g):
    rg=g[g.PLAYOFF==0]
    lp=g[g.LOW_PRESSURE==1]; pr=g[g.PRESS==1]
    gp=rg.DATE.drop_duplicates().sort_values()
    early=rg[rg.DATE.isin(gp.iloc[:20])]; late=rg[rg.DATE.isin(gp.iloc[-20:])] if len(gp)>=40 else rg.iloc[0:0]
    # game-to-game consistency: SD of per-game FT% (games with >=4 FTA)
    pg=rg.groupby('GAME_ID').MADE.agg(['size','mean']); pg=pg[pg['size']>=4]
    return pd.Series(dict(PLAYER_NAME=g.PLAYER_NAME.iloc[0],fta=len(g),ft_pct=g.MADE.mean(),
        season_min=g.SEASON_MIN.iloc[0],season_gp=g.SEASON_GP.iloc[0],
        lowpress_fta=len(lp),lowpress_ft_pct=lp.MADE.mean() if len(lp) else np.nan,
        press_fta=len(pr),press_ft_pct=pr.MADE.mean() if len(pr) else np.nan,
        press_minus_lowpress_pp=100*(pr.MADE.mean()-lp.MADE.mean()) if len(pr) and len(lp) else np.nan,
        first20g_fta=len(early),first20g_ft_pct=early.MADE.mean() if len(early) else np.nan,
        last20g_fta=len(late),last20g_ft_pct=late.MADE.mean() if len(late) else np.nan,
        pergame_ftpct_sd_games4plus=pg['mean'].std() if len(pg)>=10 else np.nan,n_games4plus=len(pg)))
P=ft.groupby(['PLAYER_ID','SEASON']).apply(ps).reset_index()
P['source']='stats.nba.com PBP via shufinskiy/nba_data; derived'
P['confidence']=np.where(P.press_fta>=40,'MEDIUM',np.where(P.press_fta>=15,'LOW','VERY LOW (tiny pressure sample)'))
P.round(4).to_csv('../out/2026-10-22_researcher-03_player_season_automaticity_proxies.csv',index=False)
# reliability of pressure gap year to year (players with >=30 pressure FTA in both seasons)
P['SY']=P.SEASON.str[:4].astype(int)
Q=P[P.press_fta>=30][['PLAYER_ID','SY','press_minus_lowpress_pp','lowpress_ft_pct','pergame_ftpct_sd_games4plus','season_min']]
M=Q.merge(Q.assign(SY=Q.SY-1),on=['PLAYER_ID','SY'],suffixes=('','_next'))
print('pairs',len(M),'r(gap,gap_next)=',round(M.press_minus_lowpress_pp.corr(M.press_minus_lowpress_pp_next),3),
      'r(lowpress,lowpress_next)=',round(M.lowpress_ft_pct.corr(M.lowpress_ft_pct_next),3))
print('r(sd_pergame, gap)=',round(Q.pergame_ftpct_sd_games4plus.corr(Q.press_minus_lowpress_pp),3),'r(season_min,gap)=',round(Q.season_min.corr(Q.press_minus_lowpress_pp),3), 'n=',len(Q))

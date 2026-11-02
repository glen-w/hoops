import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.proportion import proportion_confint
ft=pd.read_parquet('ft_enriched.parquet')
ft=ft[ft.SEASON_MIN.notna()|ft.PLAYOFF.eq(1)].copy()
lg=ft.MADE.mean(); K=20
grp=ft.groupby(['PLAYER_ID','SEASON']).MADE
ft['PS_N']=grp.transform('size'); ft['PS_M']=grp.transform('sum')
ft['BASE']=(ft.PS_M-ft.MADE+K*lg)/(ft.PS_N-1+K)
ft['BASE_LOGIT']=np.log(ft.BASE/(1-ft.BASE))
# seasonal workload quartile (regular-season minutes, within season, among players with >=1 FT)
ps=ft.drop_duplicates(['PLAYER_ID','SEASON'])[['PLAYER_ID','SEASON','SEASON_MIN']]
ps['WL_Q']=ps.groupby('SEASON').SEASON_MIN.transform(lambda s: pd.qcut(s.rank(method='first'),4,labels=['Q1_low','Q2','Q3','Q4_high']))
ft=ft.merge(ps[['PLAYER_ID','SEASON','WL_Q']],on=['PLAYER_ID','SEASON'],how='left')
ft['HIGH_WL']=(ft.WL_Q=='Q4_high').astype(int)
ft['CUM_MIN_500']=ft.CUM_MIN_BEFORE/500; ft['MIN7D_30']=ft.MIN_PRIOR_7D/30; ft['INGAME_10']=ft.INGAME_MIN_BEFORE/10
ft['CONTEXT']=np.select([ft.LATE_CLOSE==1,ft.CLUTCH==1,ft.LOW_PRESSURE==1],['late_close(<=1min,<=3pts)','clutch_other(<=5min,<=5pts)','low_pressure(Q1-3 or margin>=20)'],'other')
ft.to_parquet('ft_analysis.parquet')
# ---------- descriptive tidy table
rows=[]
def add(df,dim,lev,ctx):
    n=len(df); m=df.MADE.sum()
    if n==0: return
    lo,hi=proportion_confint(m,n,method='wilson')
    exp=df.BASE.mean()
    conf='HIGH' if n>=5000 else ('MEDIUM' if n>=1000 else 'LOW')
    rows.append(dict(season_scope='2015-16..2023-24',season_type=dim[0],context=ctx,split_dim=dim[1],split_level=lev,n_attempts=n,n_made=int(m),ft_pct=round(m/n,4),ci95_low=round(lo,4),ci95_high=round(hi,4),
        expected_pct_from_shooter_baseline=round(exp,4),diff_vs_expected_pp=round(100*(m/n-exp),2),
        source='stats.nba.com play-by-play + shotdetail via shufinskiy/nba_data (GitHub mirror); minutes reconstructed from substitutions',
        confidence=conf))
for st,sdf in [('all',ft),('regular',ft[ft.PLAYOFF==0]),('playoffs',ft[ft.PLAYOFF==1])]:
    for ctx,cdf in [('all',sdf)]+list(sdf.groupby('CONTEXT')):
        add(cdf,(st,'none'),'all',ctx)
        for col,lab in [('WL_Q','season_minutes_quartile'),('B2B','back_to_back')]:
            for lev,ldf in cdf.groupby(col,observed=True): add(ldf,(st,lab),str(lev),ctx)
        ig=pd.cut(cdf.INGAME_MIN_BEFORE,[-1,12,24,32,60],labels=['0-12','12-24','24-32','32+'])
        for lev,ldf in cdf.groupby(ig,observed=True): add(ldf,(st,'ingame_minutes_before_ft'),str(lev),ctx)
desc=pd.DataFrame(rows); desc.to_csv('../out/2026-10-22_researcher-02_ft_pressure_workload_summary.csv',index=False)
# ---------- models (cluster SE by player)
base='MADE ~ BASE_LOGIT + SECOND_OF_PAIR + TECHNICAL + C(SEASON)'
specs={
 'M1_context':base+' + LATE_CLOSE + CLUTCH + PLAYOFF + B2B + INGAME_10',
 'M2_workload':base+' + LATE_CLOSE + CLUTCH + PLAYOFF + B2B + INGAME_10 + CUM_MIN_500 + MIN7D_30 + HIGH_WL',
 'M3_interactions':base+' + LATE_CLOSE + CLUTCH + PLAYOFF + B2B + INGAME_10 + CUM_MIN_500 + MIN7D_30 + HIGH_WL + CLUTCH:HIGH_WL + CLUTCH:B2B + CLUTCH:INGAME_10 + CLUTCH:MIN7D_30 + PLAYOFF:HIGH_WL',
}
out=[]
for name,f in specs.items():
    m=smf.glm(f,data=ft,family=sm.families.Binomial()).fit(cov_type='cluster',cov_kwds={'groups':ft.PLAYER_ID.astype('int64')})
    # average marginal effect in pp for each term via derivative at mean prob
    p=m.predict(ft).mean(); scale=(m.predict(ft)*(1-m.predict(ft))).mean()
    ci=m.conf_int()
    for t in m.params.index:
        if t.startswith('C(SEASON)') or t=='Intercept': continue
        out.append(dict(model=name,term=t,coef_logodds=round(m.params[t],4),se_cluster_player=round(m.bse[t],4),ci95_low=round(ci.loc[t,0],4),ci95_high=round(ci.loc[t,1],4),p_value=round(m.pvalues[t],4),approx_ame_pp=round(100*scale*m.params[t],2),n=int(m.nobs),
            source='stats.nba.com PBP via shufinskiy/nba_data; logit with player-season leave-one-out FT% baseline; SE clustered by player',
            confidence='MEDIUM (observational; associations only)'))
    print(name, int(m.nobs)); print(m.summary().tables[1])
pd.DataFrame(out).to_csv('../out/2026-10-22_researcher-02_ft_models.csv',index=False)

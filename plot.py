import pandas as pd
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
from bokeh.plotting import figure
import math

def histvalfon(df,slidenum,typelocal):
    x=df[df['valeur_fonciere']<=10**slidenum]
    x=x[['valeur_fonciere','type_local']]
    x=x[x["type_local"]==typelocal]
    fig = px.histogram(x, x="valeur_fonciere")
    return fig
    

def valfoncbyTypelocalbydep(df,numdep):
    test=df[df["coldep"]==numdep]
    source = test[["date_mutation","valeur_fonciere","type_local"]]
    source['type_local']=source['type_local'].astype(str)
    source=source.groupby(by=["date_mutation","type_local"]).agg({"valeur_fonciere":"mean"})
    source=source.unstack()
    source.columns=df["type_local"].unique()
    source=source.reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=source['date_mutation'], y=source[source.columns[1]],
                        mode='lines',
                        name='inconnue'))
    fig.add_trace(go.Scatter(x=source['date_mutation'], y= source[source.columns[2]],
                        mode='lines',
                        name='Maison'))
    fig.add_trace(go.Scatter(x=source['date_mutation'], y=source[source.columns[3]],
                        mode='lines', name='Appartement'))
    fig.add_trace(go.Scatter(x=source['date_mutation'], y=source[source.columns[4]],
                        mode='lines', name='Dépendance'))
    fig.add_trace(go.Scatter(x=source['date_mutation'], y=source[source.columns[5]],
                        mode='lines', name='Local industriel. commercial ou assimilé'))
    return fig



def proportionTypeLocal(df,numdep,colTypelocal='type_local',colDep='coldep'):
    test=df[df[colDep]==numdep]
    test[colTypelocal] = test[colTypelocal].fillna(0)
    x = test[colTypelocal].unique()
    y = []
    for i in x:
        y.append(len(test[test[colTypelocal]==i]))
    retour=pd.DataFrame({"index":x,"value":y})
    retour["index"]=retour["index"].map(lambda x:x if x!=0 else "inconue")
    fig=alt.Chart(retour).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="index", type="nominal"),
    )
    return fig
    

    
def valFonParDep(df,colDep="coldep",colValFon="valeur_fonciere",medmean="moyenne"):
    x = df[colDep].unique()
    y=[]
    if medmean=="moyen":
        y = df[[colValFon,colDep]].groupby(by=colDep).mean()
    if medmean=="median":
        for dep in x :
            ventes_dep = df[df[colDep] == dep]
            prix_median = ventes_dep[colValFon].median()
            y.append(prix_median)
    retour=pd.DataFrame()
    retour.index=x
    retour["value"]=y
    return retour

def valFonParSufaceRBatie(df,coldep="coldep",colValFon="valeur_fonciere",colSurfaceRBatie='surface_reelle_bati',medmean="moyenne"):
    x = df[coldep].unique()
    y=[]
    if medmean=="moyen":
        y = df[[colValFon,coldep]].groupby(coldep).mean()
    if medmean=="median":
        for i in x :
            ventes_dep = df[df[coldep] == i]
            prix_m2 = pd.Series([valFon/SurfBat for valFon,SurfBat in zip(ventes_dep[colValFon],ventes_dep[colSurfaceRBatie]) if SurfBat!=0 ])
            y.append(prix_m2.median())

    retour=pd.DataFrame()
    retour.index=x
    retour["value"]=y
    return retour

def natureCulture(df,start_range,end_range):
    test=df.groupby('nature_culture').agg({"id_mutation":"count"})
    test=test.rename(columns={"id_mutation":"count"})
    test=test.sort_values("count",ascending=False).iloc[start_range:end_range]
    ind=[i for i in test.index]
    counts=[i for i  in test["count"]]

    p = figure(x_range=ind, height=350,
            toolbar_location=None, tools="")
    p.vbar(x=ind, top=counts, width=0.9)
    p.xaxis.major_label_orientation = -math.pi/3

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p
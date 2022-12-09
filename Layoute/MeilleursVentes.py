import streamlit as st
from filter import applyfilter, dep_to_num
from plot import valFonParDep,valFonParSufaceRBatie,histvalfon
from loadData import loadregion


def MeilleursVentesLayoute(selectedata,start_date,end_date):
    df=applyfilter(selectedata,start_date,end_date)
    medmean1 = st.radio(
    "Valeure Foncière moyenne ou median ? ",
    ('moyen',"median"))
    st.title(f"Valeure Foncière {medmean1} par département")
    
    st.bar_chart(valFonParDep(df,medmean=medmean1))
    medmean2 = st.radio(
        "Valeure Foncière moyenne ou median ?",
        ('moyen',"median"))
    st.title(f"Prix {medmean2} du mètre carré par département")
    
    st.bar_chart(valFonParSufaceRBatie(df,medmean=medmean2))
    
    st.title("Repartition des valeurs fonciere ")
    slidenum = st.select_slider(
    "Quelle est votre prix ?",
    options=[10**i for i in range(1,10)])
    typelocal = st.radio(
    "Quel type de bien cherchez-vous ?",
    df['type_local'].unique())
    region=loadregion()
    numdep = st.selectbox(
    'Ou voulez-vous vous installer ?',
    list(region["Département"])
    )

    st.plotly_chart(histvalfon(df,slidenum,typelocal,dep_to_num(numdep,region)))
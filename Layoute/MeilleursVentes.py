import streamlit as st
from filter import applyfilter
from plot import valFonParDep,valFonParSufaceRBatie,histvalfon


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
    "Pour les valeurs fonciere en dessous de 10 puissance ?",
    options=[i for i in range(1,10)])
    typelocal = st.radio(
    "Quel type de bien ?",
    df['type_local'].unique())

    st.plotly_chart(histvalfon(df,slidenum,typelocal))
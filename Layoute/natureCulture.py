import streamlit as st
from filter import applyfilter
from plot import natureCulture


def natureCultureLayout(selectedata,start_date,end_date):
    df=applyfilter(selectedata,start_date,end_date)
    st.title(f"Caracteritique les plus communes en {selectedata} de {start_date} à {end_date}")
    start_range,end_range = st.select_slider(
    f"Quelle caractéristiques vous interresses les plus communes ou les moins communes ?",
    options=[i for i in range(1,len(df['nature_culture'].unique())-1)],
    value=[1,10]
    )
    st.bokeh_chart(natureCulture(df,start_range,end_range))
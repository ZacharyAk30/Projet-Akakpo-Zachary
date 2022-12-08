import streamlit as st
from filter import applyfilter,mapf

def mapLayout(selectedata,start_date,end_date):
    df=applyfilter(selectedata,start_date,end_date)
    df_map=mapf(applyfilter(selectedata,start_date,end_date))
    st.dataframe(df[['longitude', 'latitude','adresse_Postal']])
    st.map(df_map)

import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def loadregion():
    region=pd.read_csv("Data/region.csv")
    return region

@st.cache(allow_output_mutation=True)
def loadataframe(selectedata,sample=True):
    if sample:
        return pd.read_csv(f"Data\sample\df{selectedata}.csv")
    else:
        return pd.read_csv(f"Data/full_{selectedata}.csv")
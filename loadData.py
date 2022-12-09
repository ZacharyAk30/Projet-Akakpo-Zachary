
import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def loadregion():
    root=r"C:/Users/zacha/OneDrive/Documents/DataViz/Projet-Akakpo-Zachary/Data"
    region=pd.read_csv(root+"/region.csv")
    return region

@st.cache(allow_output_mutation=True)
def loadataframe(selectedata,sample=True):
    root=r"C:/Users/zacha/OneDrive/Documents/DataViz/Projet-Akakpo-Zachary/Data"
    if sample:
        return pd.read_csv(root+f"\sample\df{selectedata}.csv")
    else:
        return pd.read_csv(root+f"/full_{selectedata}.csv")
import streamlit as st
import pandas as pd
import  datetime
from preprocess import prepro
from loadData import loadregion,loadataframe


def dep_to_num(dep,region):
    return int(region[region["Département"]==dep].reset_index()["num"][0])

def daterange(df,start_date,end_date):
    args = start_date.timetuple()[:6]
    start_date=datetime.datetime(*args)
    args = end_date.timetuple()[:6]
    end_date=datetime.datetime(*args)
    df["date_mutation"]=pd.to_datetime(df["date_mutation"])
    df=df[df["date_mutation"]>=start_date ]
    df=df[df["date_mutation"]<=end_date ]
    return df
    
def applyfilter(selectedata,start_date,end_date):
    df=loadataframe(selectedata)
    df=daterange(df,start_date,end_date)
    df=prepro(df)
    return df

def mapf(df):
    retour=df[['longitude', 'latitude']]
    retour["longitude"]=df["longitude"].astype(float)
    retour["latitude"]=df["latitude"].astype(float)
    retour.columns=['lon','lat']
    retour=retour.dropna()
    return retour
import streamlit as st
from streamlit_option_menu import option_menu
import datetime


def pageLayoute():
    navbar=option_menu(
            menu_title="Pages",
            options=["Caracteristique","Map","Meilleurs Ventes","Analyse sur un departement"],
            icons=["house","book","book","book"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "black"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "gray"},
            }
        )
    with st.sidebar:
        selectedata=option_menu(
                menu_title="Dataframe",
                options=["2016","2017","2018","2019","2020"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "black"},
                    "icon": {"color": "orange", "font-size": "25px"}, 
                    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "gray"},
                }
            )
        st.title("Date")
        start_date = st.date_input(
            "Start Date",
            datetime.date(int(selectedata), 1, 1)
            )
        end_date = st.date_input(
            "end Date",
            datetime.date(int(selectedata),1, 31)
            )
    return navbar , start_date ,end_date,selectedata
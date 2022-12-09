import streamlit as st
from filter import applyfilter,loadregion,dep_to_num
from plot import proportionTypeLocal,valfoncbyTypelocalbydep,histvalfon


def analyseDepLayoute(selectedata,start_date,end_date):
    df=applyfilter(selectedata,start_date,end_date)
    print(df.columns)
    region=loadregion()
    numdep = st.selectbox(
    'Quelle departement  vous interresse ?',
    list(region["Département"])
    )
    if st.button('plot'):
        nomdep=numdep
        st.title(f"Proportion de type de bien dans le departement {nomdep}")
        st.altair_chart(proportionTypeLocal(df,dep_to_num(numdep,region)))
        
        st.title(f"Valeur fonciere par type de bien dans {nomdep}")
        st.plotly_chart(valfoncbyTypelocalbydep(df,dep_to_num(numdep,region)))
    else:
        st.write("En attente de d'un departement")
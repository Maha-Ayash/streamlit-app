import pandas as pd
import streamlit as st

notenliste = pd.read_csv("notenliste.csv")

# Spalten (ähnlich Bootstrap-Grid, Gewichtung 2:1:1)
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Haupt-Inhalt")
with col2:
    st.metric("KPI 1", "42", delta="+5")


# Tabs
tab1, tab2 = st.tabs(["📈 Chart", "📋 Tabelle"])
with tab1:
    st.line_chart(notenliste)
with tab2:
    st.write(notenliste)


# selectboox
choice = st.selectbox("Wählen Sie, wie die Daten angezeigt werden", [" ","Tabelle", "Chart"])

if choice == " ":
    st.write()
elif choice == "Tabelle":
    st.write(notenliste)
elif choice == "Chart":
    st.line_chart(notenliste)    
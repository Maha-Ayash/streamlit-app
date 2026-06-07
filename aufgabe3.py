import pandas as pd
import streamlit as st

notenliste = pd.read_csv("notenliste.csv")

# Spalten (ähnlich Bootstrap-Grid, Gewichtung 2:1:1)
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Noten INFO")

# Tabs
tab1, tab2 = st.tabs(["📈 Chart", "📋 Tabelle"])
with tab1:
    st.line_chart(notenliste)
with tab2:
    st.write(notenliste)


# selectboox
choice = st.selectbox("Wählen Sie, wie die Daten angezeigt werden", [" ","Tabelle", "Chart"])

column = st.selectbox("Welche Spalte?", ["","Name", "Note"])

if choice == " ":
    st.write()
elif choice == "Tabelle":
    # st.write(notenliste)
     if choice == " ":
      st.write()
     elif column ==  "Name":
      st.write(notenliste ["Name"])
     elif column == "Note": 
      st.write(notenliste ["Note"]) 
elif choice == "Chart":
     if choice == " ":
      st.write()
     elif column ==  "Name":
      st.line_chart(notenliste ["Name"])
     elif column == "Note": 
      st.line_chart(notenliste ["Note"])   

import streamlit as st
# für APP       
def data(df):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Noten INFO")

    # Tabs
    tab1, tab2 = st.tabs(["📈 Chart", "📋 Tabelle"])
    with tab1:
        st.line_chart(df)
    with tab2:
        st.write(df)


    # selectboox
    choice = st.selectbox("Wählen Sie, wie die Daten angezeigt werden", [" ","Tabelle", "Chart"])

    column = st.selectbox("Welche Spalte?", ["","Name", "Note"])

    if choice == " ":
        st.write()
    elif choice == "Tabelle":
        # st.write(df notenliste)
        if choice == " ":
         st.write()
        elif column ==  "Name":
         st.write(df ["Name"])
        elif column == "Note": 
         st.write(df ["Note"]) 
    elif choice == "Chart":
        if choice == " ":
         st.write()
        elif column ==  "Name":
         st.line_chart(df ["Name"])
        elif column == "Note": 
         st.line_chart(df ["Note"]) 
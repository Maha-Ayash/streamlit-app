import streamlit as st

# für APP    
def counter():

    if "count" not in st.session_state:
        st.session_state.count = 0

    if st.button("Erhöhen"):
     st.session_state.count += 1
    
    if st.button('Reset'):
     st.session_state.count = 0

    st.write(f"Zähler: {st.session_state.count}") 
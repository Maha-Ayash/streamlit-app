import streamlit as st

# # FALSCH: count wird bei jedem Rerun auf 0 zurückgesetzt!
# count = 0
# if st.button("Erhöhen"):
#     count += 1
# st.write(count)  # Zeigt immer 0 oder 1, nie höher!

# ─────────────────────────────────────────

# # RICHTIG: st.session_state überlebt Reruns
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Erhöhen"):
    st.session_state.count += 1
    
if st.button('Reset'):
    st.session_state.count = 0

st.write(f"Zähler: {st.session_state.count}")  # Korrekt!    


    

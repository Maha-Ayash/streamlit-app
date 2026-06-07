import streamlit as st
# für APP
def inputs():
 
    st.title("Hallo!Mein Name ist Maha und das ist mein erstes Streamlit-Widget")
    #input Text
    name = st.text_input("Wie heißt du?")


    # Slider
    zahl = st.slider("Wähle eine Zahl", 0, 100, 50)

    # Selectbox
    choice = st.selectbox("Choose an option", ["Option ++", "Option +", "Option -"])

    # Checkbox
    agree = st.checkbox("I agree")

    if name and agree:

        st.success(f"Hallo {name}! Die Zahl ist {zahl} und du hast option {choice} ausgewhält.")
    else:
        st.info("Bitte Namen eingeben.")     
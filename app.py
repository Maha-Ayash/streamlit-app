import streamlit as st
import pandas as pd

from aufgabe1 import inputs
from aufgabe2 import counter
from aufgabe3 import data

df = pd.read_csv("notenliste.csv")
inputs()
st.divider()
counter()
st.divider()
data(df)
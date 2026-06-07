import streamlit as st
import pandas as pd

from input import inputs
from zahl import counter
from data import data

df = pd.read_csv("APP"/"notenliste.csv")
inputs()

counter()

data(df)

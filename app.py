import pandas as pd
import plotly.express as px
import streamlit as st
from pages import Pages

list_of_pages = [
    "Intro",
    "Body",
    "Ending",
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Intro":
    Pages.introduction()

elif selection == "Body":
    Pages.body()

elif selection == "Ending":
    Pages.ending()



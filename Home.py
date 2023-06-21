import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="OAI Dashboard",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


st.title("STEM Days test")

tab1, tab2 = st.tabs(["Intro", "Dataset"])

with tab1:
    st.header("Titolo")

    st.text("Fatto")

with tab2:
    countries_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/countries_df.csv")
    st.subheader("All countries")
    st.dataframe(countries_df)

    indicators_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/indicators_df.csv")
    st.subheader("All indicators")
    st.dataframe(indicators_df)








import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Single country",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

st.title("Single country")

countries_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/countries_df.csv")
indicators_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/indicators_df.csv")


selected_country = st.selectbox(
    "Choose one country",
    options = countries_df["short_name"].unique())

country_code = countries_df.loc[countries_df["short_name"] == selected_country, "country_code"].iloc[0]

st.subheader(selected_country + " country table")
df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/country_tables/" + country_code + ".csv")
st.dataframe(df)

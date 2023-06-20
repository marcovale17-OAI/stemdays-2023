import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="OAI Dashboard",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

countries_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/countries_df.csv")
indicators_df = pd.read_csv("https://storage.googleapis.com/stem-days-2023/metadata/indicators_df.csv")
st.dataframe(indicators_df)


st.title("Data availability")

col1, col2 = st.columns(2)

with col1:
   topics = st.multiselect("Select a topic", options=indicators_df["indicator_topic"].unique())
   st.write(type(topics))

with col2:
    indicators = indicators_df[indicators_df["indicator_topic"].isn(topics)]
    st.selectbox("Select an indicator", options=indicators)































import streamlit as st
import pandas as pd

st.title("HYDRA.it")

st.subheader("Steam Days 2023")

st.subheader("Open Hydra.it")

tab1 = st.tabs(["Ore musicali"])

df=pd.read_csv('C:\\Users\\stefa\\PycharmProjects\\Home\\mxmh_survey_results.csv')

pd.cut(df["Age"], bins=[0,18,25,100], labels=["Under 18", "19-25", "Over 25"])

print(df['Fav genre'].unique())

print(df.columns)

grouped = df.groupby(['Age', 'Fav genre']).aggregate({'Anxiety': "mean", 'Depression': "mean", 'Insomnia': "mean", 'OCD' : "mean"})
grouped.reset_index(inplace=True)

print(grouped.head)
print(grouped.columns)
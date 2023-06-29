import pandas as pd
import streamlit as st
import altair as alt

st.title("Data")

df = pd.read_csv('C://Users//Marco Valentini//PycharmProjects//STEM_Days//data//mxmh_survey_results.csv')

st.dataframe(df)

st.write("Numero righe: ", len(df))

options = df['Primary streaming service'].sort_values().dropna().unique()

data = df['Fav genre'].value_counts()
st.bar_chart(data)

st.selectbox("Prova", options=options)


# '#35608d', '#8a5daa', '#460082', '#f5a9bc']

filtered_df = df[(df['Hours per day'] > 1) & (df['Hours per day'] < 3)]

plot_df = pd.DataFrame(df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
plot_df["Hours per day"] = plot_df.index.values

plot = alt.Chart(plot_df).mark_bar(color='#f5a9bc').encode(
    x='Hours per day',
    y='count',
    tooltip=["Hours per day", "count"]
).interactive()

st.markdown("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

st.write(plot_df)
st.altair_chart(plot)
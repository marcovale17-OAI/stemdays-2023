import streamlit as st
import pandas as pd
import altair as alt
import os

root_data_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data"
)

df = pd.read_csv(os.path.join(root_data_path, 'mxmh_survey_results_nonmodificato.csv'))

st.title("HYDRA.it")

st.subheader("Steam Days 2023")

st.subheader("Open Hydra.it")


tab1, tab2, tab3 = st.tabs(["Ore musicali", "Musica lavorando", "Preferenze musicali"])

with tab1:
    st.text("Breve riassunto")
    st.text("Testo lungo")
    plot_df = pd.DataFrame(df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
    plot_df["Hours per day"] = plot_df.index.values
    plot = alt.Chart(plot_df).mark_bar().encode(
        x='Hours per day',
        y='count',
        tooltip=["Hours per day", "count"]
    ).interactive()
    st.altair_chart(plot, use_container_width=True)

with tab2:
    st.text("Breve riassunto")
    st.text("Testo lungo")
    options = ("Ascoltano musica al lavoro", "Non ascoltano muscica a lavoro")
    grafico = st.radio("Vuoi sapere se le persone", options=options)
    if grafico == "Ascoltano musica al lavoro":
        filtered_df = df[df['While working']=="Yes"]
        plot_df = pd.DataFrame(filtered_df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
        plot_df["Hours per day"] = plot_df.index.values
        plot = alt.Chart(plot_df).mark_bar().encode(
            x='Hours per day',
            y='count',
            tooltip=["Hours per day", "count"]
        ).interactive()
        st.altair_chart(plot, use_container_width=True)

    else:
        filtered_df = df[df['While working'] == "No"]
        plot_df = pd.DataFrame(df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
        plot_df["Hours per day"] = plot_df.index.values
        plot = alt.Chart(plot_df).mark_bar().encode(
            x='Hours per day',
            y='count',
            tooltip=["Hours per day", "count"]
        ).interactive()
        st.altair_chart(plot, use_container_width=True)

with tab3:
    st.text("Breve riassunto")
    st.text("Testo lungo")

    base = alt.Chart(df).encode(
        x=alt.X('count():Q'),
        y=alt.Y('Fav genre:N', sort=alt.EncodingSortField(field="Fav genre", op="count", order='descending')),
        text='count()',
        tooltip=['count()', 'Fav genre']
    )
    base.mark_bar().interactive() + base.mark_text(align='left', dx=2)

st.divider()
st.text("Nomi Cognomi, Ruoli ecc...")
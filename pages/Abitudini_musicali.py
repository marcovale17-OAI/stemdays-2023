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


tab1, tab2, tab3 = st.tabs(["Ore musicali", "Musica lavorando", "Preferenze musicali"])

with tab1:
    st.subheader("Abitudini musicali di tutto il campione di persone")
    st.markdown("Questo grafico mostra l’ascolto medio quotidiano di musica delle persone. È possibile notare che la maggioranza degli individui ascolta musica per due ore al giorno e che in media il tempo compreso tra un ora e sei ore al giorno è il range più frequente.")
    plot_df = pd.DataFrame(df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
    plot_df["Hours per day"] = plot_df.index.values
    plot_df["Hours per day"] = plot_df["Hours per day"].round()
    plot = alt.Chart(plot_df).mark_bar().encode(
        x=alt.X('Hours per day', title="Ore di ascolto al giorno"),
        y=alt.Y('count', title="Numero di persone"),
        tooltip=[alt.Tooltip("Hours per day", title="Ore di ascolto al giorno"), alt.Tooltip("count", title='Numero di persone')]
    ).interactive()
    st.altair_chart(plot, use_container_width=True)

with tab2:
    st.subheader("Abitudini musicali divisi tra chi ascolta musica a lavoro e chi no")
    st.markdown("""Questo grafico mostra l’ascolto medio quotidiano di musica delle persone. È possibile notare che la maggioranza degli individui ascolta musica per due ore al giorno e che in media il tempo compreso tra un ora e sei ore al giorno è il range più frequente.
    \nLe due sottopopolazioni non dimostrano differenze significative. """)
    options = ("Ascoltano musica al lavoro", "Non ascoltano muscica a lavoro")
    grafico = st.radio("Vuoi sapere se le persone", options=options)
    if grafico == "Ascoltano musica al lavoro":
        filtered_df = df[df['While working']=="Yes"]
        plot_df = pd.DataFrame(filtered_df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
        plot_df["Hours per day"] = plot_df.index.values
        plot_df["Hours per day"] = plot_df["Hours per day"].round()
        plot = alt.Chart(plot_df).mark_bar().encode(
            x=alt.X('Hours per day', title="Ore di ascolto al giorno"),
            y=alt.Y('count', title="Numero di persone"),
            tooltip=[alt.Tooltip("Hours per day", title="Ore di ascolto al giorno"), alt.Tooltip("count", title='Numero di persone')]
        ).interactive()
        st.altair_chart(plot, use_container_width=True)

    else:
        filtered_df = df[df['While working'] == "No"]
        plot_df = pd.DataFrame(df['Hours per day'].value_counts()).rename(columns={"Hours per day": "count"})
        plot_df["Hours per day"] = plot_df.index.values
        plot = alt.Chart(plot_df).mark_bar().encode(
            x=alt.X('Hours per day', title="Ore di ascolto al giorno"),
            y=alt.Y('count', title="Numero di persone"),
            tooltip=[alt.Tooltip("Hours per day", title="Ore di ascolto al giorno"), alt.Tooltip("count", title='Numero di persone')]
        ).interactive()
        st.altair_chart(plot, use_container_width=True)

with tab3:
    st.subheader("Abitudini musicali di tutto il campione")
    st.markdown("Il grafico sottostante rappresenta quali sono i generi preferiti dalle persone. Il rock è il genere prediletto, seguito dal pop e dal metal, mentre il meno ascoltato è il gospel.")

    base = alt.Chart(df).mark_bar().encode(
        x=alt.X('count():Q', title='Numero di persone'),
        y=alt.Y('Fav genre:N', title='Genere preferito', sort=alt.EncodingSortField(field="Fav genre", op="count", order='descending')),
        text='count()',
        tooltip=[alt.Tooltip('count()', title='Numero di persone'),
                 alt.Tooltip('Fav genre', title='Genere preferito')]
    ).interactive()
    st.altair_chart(base, use_container_width=True)
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

st.subheader("Abitudini musicali di tutto il campione")
st.markdown("""Questo grafico mette a confronto i generi musicali e i disturbi mentali degli ascoltatori.
            Come si può notare il rock e il folk sono strettamente connessi alla sfera dell’ansia, mentre il low fi alla depressione. invece, l’OCD non sembra avere correlazioni strette con tutti i  generi musicali."
            Bisogna però specificare che il grafico può essere lievemente sfalsato, in quanto il numero di persone che ascoltano i vari generi varia molto, un chiaro esempio è rappresentato dalla differenza di ascoltatori del gospel (2) e del rock (180).""")

grouped_df = df.groupby("Fav genre", as_index=False)[['Anxiety', 'Depression', 'Insomnia', 'OCD']].mean()
grouped_df_long_form = pd.melt(
    grouped_df, id_vars=['Fav genre'],
    value_vars=['Anxiety', 'Depression', 'Insomnia', 'OCD'],
    var_name='Disease', value_name='Average_value'
)
plot = alt.Chart(grouped_df_long_form).mark_rect(size=60).encode(
    x=alt.X('Disease', title='Autovalutazione'),
    y=alt.Y('Fav genre', title='Genere musicale preferito'),
    color=alt.Color('Average_value', title='Valore medio'),
    tooltip=list(grouped_df_long_form.columns)
).interactive()
st.altair_chart(plot, use_container_width=True)

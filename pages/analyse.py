import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os  
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from style import apply_style   
from data import load_data

st.set_page_config(page_title="Workout — Analyse", page_icon="⚡", layout="centered", initial_sidebar_state="collapsed")
apply_style()

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

data = load_data()
sessions = data["sessions"] if data else []

st.markdown('<div class="title">ANALYSE <span class="accent">PERFORMANCES</span></div>', unsafe_allow_html=True)

rows = []
for session in sessions:
    for exercise, reps in session["reps"].items():
        rows.append({
            "date": session["timestamp"],
            "seance_id": session["seance_id"],
            "exercise": exercise,
            "reps": sum(reps)
        })

df = pd.DataFrame(rows)


#Filtrer la seance
seances_dispo = df["seance_id"].unique().tolist()
seances_choisie = st.selectbox("Sélectionne une séance", options=seances_dispo)

# Filtrer les exercices
df_filtre = df[df["seance_id"] == seances_choisie]
exercices_dispo = df_filtre["exercise"].unique().tolist()
exercices_choisis = st.selectbox("Sélectionne un exercice", options=exercices_dispo)

#dataframe final filtré
df_graph = df_filtre[df_filtre["exercise"] == exercices_choisis]

fig = px.line(df_graph, x="date", y="reps", title=f"Évolution des reps pour {exercices_choisis}",template="plotly_dark")
fig.update_traces(line_color="#f5c400",marker_color="#f5c400")
fig.update_layout(paper_bgcolor="#111", plot_bgcolor="#111")
st.plotly_chart(fig, use_container_width=True)



# ─── RETOUR ───────────────────────────────────────────────────────────────────

st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
if st.button("← Retour", key="back"):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from style import apply_style

st.set_page_config(page_title="Workout — Séances", page_icon="⚡", layout="centered", initial_sidebar_state="collapsed")
apply_style()

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

# ─── SÉANCES ──────────────────────────────────────────────────────────────────

SEANCES = [
    {
        "id": "seance_1",
        "name": "SÉANCE 1",
        "tag": "UPPER BODY",
        "desc": "Tractions · Pompes · Tirage · Dips · Traction biceps · Pompes diamant",
        "groups": [
            {"group": "Groupe A - Tractions/Pompes", "exercises": ["Tractions", "Pompes"],"series": 4, "seuils":{"Tractions":10,"Pompes":15}},
            {"group": "Groupe B - Tirage/Dips", "exercises": ["Tirage", "Dips"],"series": 4, "seuils":{"Tirage":12,"Dips":15}},
            {"group": "Groupe C - Traction biceps/Pompes diamant", "exercises": ["Traction biceps", "Pompes diamant"],"series": 3, "seuils":{"Traction biceps":10,"Pompes diamant":15}},
        ],
        "rest": 60,
    },
    {
        "id": "seance_2",
        "name": "SÉANCE 2",
        "tag": "TEST",
        "desc": "Squat · Fentes — séance de test",
        "groups": [
            {"group": "Groupe Test", "exercises": ["Squat", "Fentes"],"series": 3, "seuils":{"Squat":20,"Fentes":20}},
        ],
        "rest": 45,
    },
]

if "selected_seance_id" not in st.session_state:
    st.session_state.selected_seance_id = None

# ─── HEADER ───────────────────────────────────────────────────────────────────

st.markdown('<div class="title">CHOIX <span class="accent">SÉANCE</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sélectionne ton entraînement</div>', unsafe_allow_html=True)

# ─── CARTES ───────────────────────────────────────────────────────────────────

for seance in SEANCES:
    is_selected = st.session_state.selected_seance_id == seance["id"]
    card_class = "card selected" if is_selected else "card"
    total_exos = sum(len(g["exercises"]) for g in seance["groups"])
    total_series = sum(len(g["exercises"])*(g["series"]) for g in seance["groups"])
    st.markdown(f"""
        <div class="{card_class}">
            <div class="card-row">
                <div class="card-title">{seance['name']}</div>
                <div class="badge">{seance['tag']}</div>
            </div>
            <div class="card-desc">{seance['desc']}</div>
            <div class="card-meta">
                <div class="meta">Exercices&nbsp;<span>{total_exos}</span></div>
                <div class="meta">Total Séries&nbsp;<span>{total_series}</span></div>
                <div class="meta">Repos&nbsp;<span>{seance['rest']}s</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    btn_class = "btn-active" if is_selected else ""
    label = "✦ Sélectionnée" if is_selected else f"Sélectionner {seance['name']}"

    st.markdown(f'<div class="{btn_class}">', unsafe_allow_html=True)
    if st.button(label, key=f"btn_{seance['id']}"):
        st.session_state.selected_seance_id = seance["id"]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ─── DÉMARRER ─────────────────────────────────────────────────────────────────

st.markdown("<br>", unsafe_allow_html=True)
selected = next((s for s in SEANCES if s["id"] == st.session_state.selected_seance_id), None)

st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
if selected:
    if st.button("⚡  DÉMARRER LA SÉANCE", key="start"):
        st.session_state.seance_active = selected
        st.switch_page("pages/seance.py")
else:
    st.button("⚡  DÉMARRER LA SÉANCE", key="start_disabled", disabled=True)
st.markdown('</div>', unsafe_allow_html=True)

#Analyse
st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
if st.button("📊 Analyse des performances"):
    st.switch_page("pages/analyse.py")
st.markdown('</div>', unsafe_allow_html=True)

# ─── RETOUR ───────────────────────────────────────────────────────────────────

st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
if st.button("← Retour", key="back"):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)
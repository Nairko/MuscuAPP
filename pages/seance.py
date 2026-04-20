import streamlit as st
from data import get_last_session_reps, save_session
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from style import apply_style

st.set_page_config(page_title="Workout — Séance", page_icon="⚡", layout="centered", initial_sidebar_state="collapsed")
apply_style()

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

seance = st.session_state.get("seance_active")
if not seance:
    st.switch_page("pages/selection.py")

tag = seance["tag"] if seance.get("tag") else "SANS ÉTIQUETTE"
premier_groupe = seance["groups"][0]


def build_plan(seance):
    plan  = []
    for group in seance["groups"]:
        for serie in range(1, group["series"]+1):
            for exercise in group["exercises"]:
                plan.append({
                    "group": group["group"],
                    "exercise": exercise,
                    "serie": serie
                })
    return plan

plan = build_plan(seance)

if "step" not in st.session_state:
    st.session_state.step = 0

if "phase" not in st.session_state:
    st.session_state.phase = "work"  # work, rest, transition

if "reps_today" not in st.session_state:
    st.session_state.reps_today = {}

current = plan[st.session_state.step]

group_actuel = current["group"]
exercice_actuel = current["exercise"]
serie_actuelle = current["serie"]

st.markdown(f'<div class="title">{seance["name"]} <span class="accent">{tag}</span></div>', unsafe_allow_html=True)

# Si la séance n'est pas terminée, afficher le bouton abandonner 
if st.session_state.phase != "done":
    st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
    if st.button("x Abandonner la séance"):
        for key in ["step", "phase", "reps_today","saved"]:
            if key in st.session_state:
                del st.session_state[key]
        st.switch_page("pages/selection.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
            <div class ="badge">{current['group']}</div>
            <div class="card-title">{exercice_actuel}</div>
            <div class="subtitle">Séries: {serie_actuelle}</div>
</div>
""", unsafe_allow_html=True)
col_gauche, col_droite = st.columns(2)

with col_gauche:
    last = get_last_session_reps(seance["id"], exercice_actuel)
    if last:
        st.markdown(f'<div class="subtitle">Dernière fois : {sum(last)} reps</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="subtitle">Premier passage</div>', unsafe_allow_html=True)
    reps = st.number_input("Reps", min_value=0, max_value=99, value=10, key=f"reps_{st.session_state.step}")


#seance["rest"]
with col_droite:
    if st.session_state.phase == "rest":
        import time
        placeholder = st.empty()
        for i in range(2, 0, -1):
            placeholder.markdown(f'<div class="timer">{i}s</div>', unsafe_allow_html=True)
            time.sleep(1)
        st.session_state.phase = "work"
        st.rerun()

# ── Bouton valider — pleine largeur en bas ──
if st.session_state.phase == "work":
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("✓ VALIDER LES REPS", key=f"valider_{st.session_state.step}"):
        if exercice_actuel not in st.session_state.reps_today:
            st.session_state.reps_today[exercice_actuel] = []
        st.session_state.reps_today[exercice_actuel].append(reps)
        if st.session_state.step + 1 >= len(plan):
            st.session_state.phase = "done"
        else:
            st.session_state.step += 1
            st.session_state.phase = "rest"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.phase == "done":
    if not st.session_state.get("saved"):
        save_session(seance["id"], st.session_state.reps_today)
        st.session_state.saved = True
    
    st.markdown('<div class="title">SÉANCE <span class="accent">TERMINÉE</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Récapitulatif</div>', unsafe_allow_html=True)
    
    for exercice, reps_liste in st.session_state.reps_today.items():
        total = sum(reps_liste)
        last = get_last_session_reps(seance["id"], exercice)
        last_total = sum(last) if last else None
        
        if last_total:
            diff = total - last_total
            diff_str = f"+{diff}" if diff >= 0 else str(diff)
        else:
            diff_str = "premier passage"
        
        for group in seance["groups"]:
            if exercice in group["exercises"]:
                seuil = group["seuils"][exercice]
                if total >= seuil*group["series"]:
                    to_easy_str = "Félicitation, augmentent la difficulté⭐"
                else:
                    to_easy_str = ""
                break
        
        st.markdown(f"""
        <div class="card">
            <div class="card-row">
                <div class="card-title">{exercice}</div>
                <div class="badge">{diff_str}</div>
            </div>
            <div class="subtitle">Total : {total} reps — {reps_liste}</div>
            <div class="success">{to_easy_str}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("← RETOUR ACCUEIL"):
        for key in ["step", "phase", "reps_today"]:
            del st.session_state[key]
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)
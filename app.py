import streamlit as st
import hashlib
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from style import apply_style

st.set_page_config(page_title="Workout", page_icon="⚡", layout="centered", initial_sidebar_state="collapsed")
apply_style()

# ─── USERS ────────────────────────────────────────────────────────────────────

# Générer un hash : python -c "import hashlib; print(hashlib.sha256('TON_MDP'.encode()).hexdigest())"

USERS = {
    "nathan": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # 123456
}

def check_login(username, password):
    h = hashlib.sha256(password.encode()).hexdigest()
    return USERS.get(username.lower().strip()) == h

# ─── STATE ────────────────────────────────────────────────────────────────────

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ══════════════════════════════════════════════════════════════════════════════
# PAGE LOGIN
# ══════════════════════════════════════════════════════════════════════════════

if not st.session_state.logged_in:

    st.markdown('<div class="title"><span class="accent">WORKOUT</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Training Tracker</div>', unsafe_allow_html=True)

    st.markdown('<div class="label">Identifiant</div>', unsafe_allow_html=True)
    username = st.text_input("u", placeholder="Ton pseudo")

    st.markdown('<div class="label" style="margin-top:16px;">Mot de passe</div>', unsafe_allow_html=True)
    password = st.text_input("p", placeholder="••••••••", type="password")

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("CONNEXION"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username.strip().lower()
            st.rerun()
        else:
            st.error("Identifiant ou mot de passe incorrect.")
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE HOME
# ══════════════════════════════════════════════════════════════════════════════

else:
    name = st.session_state.get("username", "").capitalize()

    st.markdown(f'<div class="subtitle">Bienvenue,</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="title">{name}<span class="accent">.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle" style="margin-bottom:64px;">Prêt à attaquer ?</div>', unsafe_allow_html=True)

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("⚡  DÉMARRER"):
        st.switch_page("pages/selection.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
    if st.button("Se déconnecter"):
        st.session_state.logged_in = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
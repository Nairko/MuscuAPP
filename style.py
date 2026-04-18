import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [data-testid="stAppViewContainer"] { background: #0a0a0a !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    #[data-testid="stToolbar"] { display: none; }
    [data-testid="stSidebarNav"] { display: none; }
    .block-container { padding: 2rem 1.5rem 4rem !important; max-width: 480px !important; }

    /* ── Typo ── */
    .title {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 52px; color: #f0f0f0;
        letter-spacing: 4px; margin-bottom: 2px;
    }
    .accent { color: #f5c400; }
    .subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px; color: #666;
        letter-spacing: 3px; text-transform: uppercase; margin-bottom: 36px;
    }
    .label {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px; color: #555;
        letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px;
    }
    
    .success {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px; color: #9efd38;
        letter-spacing: 3px; text-transform: uppercase; margin-bottom: 36px;
    }

    /* ── Carte générique ── */
    .card {
        background: #111; border: 1px solid #222;
        border-radius: 16px; padding: 22px; margin-bottom: 6px;
    }
    .card.selected { border: 2px solid #f5c400; background: #131208; }
    .card-title {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 34px; color: #f0f0f0; letter-spacing: 2px; line-height: 1;
    }
    .card-desc { font-family: 'DM Sans', sans-serif; font-size: 13px; color: #888; line-height: 1.6; margin: 10px 0 14px; }
    .card-row { display: flex; justify-content: space-between; align-items: flex-start; }
    .card-meta { display: flex; gap: 20px; }
    .meta { font-family: 'DM Sans', sans-serif; font-size: 12px; color: #666; }
    .meta span { color: #aaa; font-weight: 500; }

    /* ── Badge ── */
    .badge {
        font-family: 'DM Sans', sans-serif; font-size: 10px; font-weight: 500;
        color: #f5c400; background: rgba(245,196,0,0.08);
        border: 1px solid rgba(245,196,0,0.2);
        border-radius: 5px; padding: 3px 9px; letter-spacing: 1.5px;
    }

    /* ── Inputs ── */
    .stTextInput > label { display: none !important; }
    .stTextInput > div > div > input {
        background: #141414 !important; border: 1px solid #242424 !important;
        border-radius: 10px !important; color: #f0f0f0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 16px !important; padding: 12px 16px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #f5c400 !important;
        box-shadow: 0 0 0 3px rgba(245,196,0,0.12) !important;
    }

    /* ── Boutons ── */
    .stButton > button {
        width: 100% !important; border-radius: 10px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14px !important; padding: 10px !important;
        background: #1a1a1a !important; color: #555 !important;
        border: 1px solid #222 !important;
        margin-top: 0 !important; margin-bottom: 10px !important;
    }
    .stButton > button:hover { border-color: #f5c400 !important; color: #f5c400 !important; }

    /* Bouton primaire jaune */
    .btn-primary > .stButton > button {
        background: #f5c400 !important; color: #0a0a0a !important;
        border: none !important; font-family: 'Bebas Neue', sans-serif !important;
        font-size: 22px !important; letter-spacing: 3px !important; padding: 14px !important;
    }
    .btn-primary > .stButton > button:hover { opacity: 0.88 !important; }
    .btn-primary > .stButton > button:disabled { background: #1a1a1a !important; color: #2a2a2a !important; }

    /* Bouton sélectionné */
    .btn-active > .stButton > button {
        background: rgba(245,196,0,0.08) !important;
        color: #f5c400 !important; border: 1px solid rgba(245,196,0,0.3) !important;
    }

    /* Bouton discret */
    .btn-ghost > .stButton > button {
        background: transparent !important; color: #2a2a2a !important;
        border: 1px solid #1a1a1a !important; font-size: 13px !important;
    }
    .btn-ghost > .stButton > button:hover { color: #555 !important; border-color: #333 !important; }
    /* Timer */
    .timer {
        font-family: 'Bebas Neue', sans-serif; font-size: 62px; color: #f5c400;
        text-align: center;
        margin-top: 28px;
    }
    </style>
    """, unsafe_allow_html=True)
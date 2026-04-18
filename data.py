import json
import gspread
import streamlit as st
from datetime import datetime
from google.oauth2.service_account import Credentials

# ─── CONNEXION ────────────────────────────────────────────────────────────────
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

@st.cache_resource
def get_sheet():
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    sh = client.open("workout_data")
    try:
        worksheet = sh.worksheet("sessions")
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title="sessions", rows=1000, cols=4)
        worksheet.append_row(["timestamp", "seance_id", "exercise", "reps"])
    return worksheet

@st.cache_data(ttl=60)
def load_data():
    worksheet = get_sheet()
    rows = worksheet.get_all_records()
    sessions = {}
    for row in rows:
        key = (row["timestamp"], row["seance_id"])
        if key not in sessions:
            sessions[key] = {
                "timestamp": row["timestamp"],
                "seance_id": row["seance_id"],
                "reps": {}
            }
        sessions[key]["reps"][row["exercise"]] = json.loads(row["reps"])
    return {"sessions": list(sessions.values())}

def save_session(seance_id, reps_dict):
    """Sauvegarde une séance — une ligne par exercice."""
    worksheet = get_sheet()
    timestamp = datetime.now().strftime("%Y-%m-%d")
    for exercise, reps in reps_dict.items():
        worksheet.append_row([timestamp, seance_id, exercise, json.dumps(reps)])
    load_data.clear()  # vide le cache après sauvegarde

def get_last_session_reps(seance_id, exercise_name):
    """Retourne la liste de reps de la dernière séance pour un exercice."""
    data = load_data()
    sessions = [s for s in data["sessions"] if s["seance_id"] == seance_id]
    if not sessions:
        return None
    derniere = sessions[-1]
    return derniere["reps"].get(exercise_name)
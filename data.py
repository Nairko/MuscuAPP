import json
import os  
from datetime import datetime


def load_data(file_path="workout_data.json"):
    if not os.path.exists(file_path):
        return {"sessions": []}
    else:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    
def save_session(seance_id, reps_dict, file_path="workout_data.json"):
    data = load_data(file_path)
    session_entry = {
        "seance_id": seance_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "reps": reps_dict
    }
    data["sessions"].append(session_entry)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def get_last_session_reps(seance_id, exercise_name,file_path="workout_data.json"):
    data = load_data(file_path)
    sessions = [s for s in data["sessions"] if s["seance_id"] == seance_id]
    if not sessions:
        return None
    derniere= sessions[-1]
    return derniere["reps"].get(exercise_name)
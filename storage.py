# storage.py
import json
from pathlib import Path


FILE = Path("users.json")

def load_users():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return {}

def save_users(users):
    FILE.write_text(json.dumps(users, indent=2, ensure_ascii=False), encoding="utf-8")

def init_user(users, uid):
    if str(uid) not in users:
        users[str(uid)] = {"count": 0, "mode": ["Therapist", "Schizo", "God", "InnerVoice", "MirrorSelf",
    "Split", "Persona", "Apocalypse", "Confession",
    "Smart", "Creative", "Humor"], "is_pro": False, "history": []}


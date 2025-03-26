import json
import os

KRL_FILE = "krl.json"

def load_krl():
    if not os.path.exists(KRL_FILE):
        return []
    with open(KRL_FILE, "r") as file:
        return json.load(file)

def save_krl(krl):
    with open(KRL_FILE, "w") as file:
        json.dump(krl, file, indent=4)

def revoke_key(key_name):
    krl = load_krl()
    if key_name not in krl:
        krl.append(key_name)
        save_krl(krl)
        print(f"❌ Key '{key_name}' revoked!")

def check_key_status(key_name):
    return key_name in load_krl()

def remove_key_revocation(key_name):
    krl = load_krl()
    if key_name in krl:
        krl.remove(key_name)
        save_krl(krl)
        print(f"✅ Key '{key_name}' unrevoked!")

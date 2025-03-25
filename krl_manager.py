import json

KRL_FILE = "krl.json"

def revoke_key(key_filename):
    """Revoke a key and store it in the KRL."""
    try:
        with open(KRL_FILE, "r") as krl_file:
            revoked_keys = json.load(krl_file)
    except (FileNotFoundError, json.JSONDecodeError):
        revoked_keys = []

    if key_filename not in revoked_keys:
        revoked_keys.append(key_filename)
        with open(KRL_FILE, "w") as krl_file:
            json.dump(revoked_keys, krl_file)
        print(f"❌ Key '{key_filename}' revoked!")
    else:
        print(f"⚠️ Key '{key_filename}' is already revoked.")

def check_key_status(key_filename):
    """Check if a key is revoked."""
    try:
        with open(KRL_FILE, "r") as krl_file:
            revoked_keys = json.load(krl_file)
        if key_filename in revoked_keys:
            print(f"❌ Key '{key_filename}' is revoked!")
            return True
    except FileNotFoundError:
        pass
    return False

def remove_key_revocation(key_filename):
    """Remove a key from the KRL, effectively unrevoking it."""
    try:
        with open(KRL_FILE, "r") as krl_file:
            revoked_keys = json.load(krl_file)
    except (FileNotFoundError, json.JSONDecodeError):
        revoked_keys = []

    if key_filename in revoked_keys:
        revoked_keys.remove(key_filename)
        with open(KRL_FILE, "w") as krl_file:
            json.dump(revoked_keys, krl_file)
        print(f"✅ Key '{key_filename}' removed from revocation list!")
    else:
        print(f"ℹ️ Key '{key_filename}' was not revoked.")

if __name__ == "__main__":
    key_to_revoke = input("Enter the key filename to revoke: ")
    revoke_key(key_to_revoke)

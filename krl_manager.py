import os

KRL_FILE = "revoked_keys.txt"

def check_key_status(key_file):
    """ Check if the key is revoked """
    if not os.path.exists(KRL_FILE):
        return False  # No revocations exist yet

    with open(KRL_FILE, "r") as file:
        revoked_keys = file.read().splitlines()

    return key_file in revoked_keys

def revoke_key(key_file):
    """ Revoke a key and log it in the KRL file """
    if not check_key_status(key_file):
        with open(KRL_FILE, "a") as file:
            file.write(key_file + "\n")
        print(f"❌ Key '{key_file}' revoked!")
    else:
        print(f"⚠️ Key '{key_file}' is already revoked.")

def remove_key_revocation(key_file):
    """ Remove a key from the revocation list """
    if not os.path.exists(KRL_FILE):
        print("⚠️ No revoked keys found.")
        return
    
    with open(KRL_FILE, "r") as file:
        revoked_keys = file.read().splitlines()

    if key_file in revoked_keys:
        revoked_keys.remove(key_file)
        with open(KRL_FILE, "w") as file:
            file.write("\n".join(revoked_keys) + "\n")
        print(f"✅ Key '{key_file}' revocation removed!")
    else:
        print(f"⚠️ Key '{key_file}' is not revoked.")

if __name__ == "__main__":
    # Example usage
    revoke_key("private_key.pem")
    remove_key_revocation("private_key.pem")

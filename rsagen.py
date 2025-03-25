import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import krl_manager  # Import the KRL manager functions

def generate_and_save_keys():
    """Generate and store RSA keys securely."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Remove any existing revocation for these filenames before saving new keys
    krl_manager.remove_key_revocation("private_key.pem")
    krl_manager.remove_key_revocation("public_key.pem")

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("✅ RSA Keys Generated and Saved!")

if __name__ == "__main__":
    generate_and_save_keys()

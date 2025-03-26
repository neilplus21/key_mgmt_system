from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import krl_manager

def sign_message(message):
    if krl_manager.check_key_status("private_key.pem"):
        print("❌ Cannot sign: Private key is revoked!")
        return None

    with open("private_key.pem", "rb") as priv_file:
        private_key = serialization.load_pem_private_key(priv_file.read(), password=None)

    return private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

def verify_signature(message, signature):
    with open("public_key.pem", "rb") as pub_file:
        public_key = serialization.load_pem_public_key(pub_file.read())

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("✅ Signature Verified!")
    except:
        print("❌ Signature Verification Failed!")

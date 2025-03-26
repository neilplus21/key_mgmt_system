from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import krl_manager

def verify_certificate():
    try:
        with open("certificate.pem", "rb") as cert_file:
            cert = x509.load_pem_x509_certificate(cert_file.read())

        if cert.not_valid_before <= datetime.datetime.utcnow() <= cert.not_valid_after:
            print("✅ Certificate is valid!")
            return True
        else:
            print("❌ Certificate expired or not yet valid!")
            return False
    except:
        print("❌ Invalid certificate!")
        return False

def sign_and_verify():
    if krl_manager.check_key_status("private_key.pem"):
        print("❌ Cannot sign: Private key is revoked!")
        return

    if not verify_certificate():
        print("❌ Cannot sign: Certificate invalid!")
        return

    with open("private_key.pem", "rb") as priv_file:
        private_key = serialization.load_pem_private_key(priv_file.read(), password=None)

    with open("public_key.pem", "rb") as pub_file:
        public_key = serialization.load_pem_public_key(pub_file.read())

    message = b"Verify this message"
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

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

if __name__ == "__main__":
    sign_and_verify()

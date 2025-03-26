from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
import datetime

CERT_FILE = "certificate.pem"

def generate_x509_certificate():
    with open("private_key.pem", "rb") as priv_file:
        private_key = serialization.load_pem_private_key(priv_file.read(), password=None)

    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Karnataka"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Bangalore"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "SecureKey Management"),
        x509.NameAttribute(NameOID.COMMON_NAME, "securekey.local")
    ])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .sign(private_key, hashes.SHA256())
    )

    with open(CERT_FILE, "wb") as cert_file:
        cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

    print("✅ X.509 Certificate Generated Successfully!")

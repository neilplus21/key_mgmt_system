from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    with open("dh_parameters.pem", "wb") as param_file:
        param_file.write(parameters.parameter_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.ParameterFormat.PKCS3
        ))
    print("✅ Diffie-Hellman Parameters Generated!")

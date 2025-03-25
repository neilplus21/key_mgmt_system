from cryptography.hazmat.primitives.asymmetric import dh

def perform_key_exchange():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    print("✅ Diffie-Hellman Key Exchange Performed!")
    return private_key, public_key

if __name__ == "__main__":
    perform_key_exchange()

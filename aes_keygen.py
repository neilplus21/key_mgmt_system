import os

def generate_aes_key():
    aes_key = os.urandom(32)  # Generate a 256-bit AES key
    with open("aes_key.bin", "wb") as key_file:
        key_file.write(aes_key)
    print("✅ AES Key Generated and Saved!")

if __name__ == "__main__":
    generate_aes_key()

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

KEY_FILE = "aes_key.bin"

def generate_aes_key():
    key = os.urandom(32)  # 256-bit AES key
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("✅ AES Key Generated Successfully!")

def load_aes_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

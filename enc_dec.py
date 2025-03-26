from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded_message = message + b" " * (16 - len(message) % 16)
    return iv + encryptor.update(padded_message) + encryptor.finalize()

def decrypt_message(encrypted_data, key):
    iv, encrypted_message = encrypted_data[:16], encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_message) + decryptor.finalize()

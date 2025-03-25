from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def encrypt_decrypt_demo():
    key = os.urandom(32)  # AES-256 key
    iv = os.urandom(16)  # Initialization Vector (IV)
    message = b"Confidential Data"  # Original data

    # Padding (PKCS7)
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message) + padder.finalize()

    # Encrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    print("✅ Encrypted:", ciphertext)

    # Decrypt
    decryptor = cipher.decryptor()
    decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove Padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded_message) + unpadder.finalize()

    print("✅ Decrypted:", plaintext)

if __name__ == "__main__":
    encrypt_decrypt_demo()

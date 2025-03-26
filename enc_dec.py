from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_decrypt_demo():
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)  # 128-bit IV
    message = b"Confidential Data   "  # 16-byte padded

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    print("✅ Encrypted:", ciphertext)

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    print("✅ Decrypted:", plaintext)

if __name__ == "__main__":
    encrypt_decrypt_demo()

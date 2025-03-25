import aes_keygen
import rsagen
import key_ex
import enc_dec
import authentication
import krl_manager

def main():
    print("\n🔹 Secure Key Management System 🔹")
    print("1. Generate AES Key")
    print("2. Generate RSA Keys")
    print("3. Perform Key Exchange")
    print("4. Encrypt & Decrypt Data")
    print("5. Sign & Verify Messages")
    print("6. Revoke Key")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        aes_keygen.generate_aes_key()
    elif choice == "2":
        rsagen.generate_and_save_keys()
    elif choice == "3":
        key_ex.perform_key_exchange()
    elif choice == "4":
        enc_dec.encrypt_decrypt_demo()
    elif choice == "5":
        authentication.sign_and_verify()
    elif choice == "6":
        key_to_revoke = input("Enter the key filename to revoke: ")
        krl_manager.revoke_key(key_to_revoke)
    elif choice == "7":
        print("Exiting...")
        exit()
    else:
        print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    while True:
        main()

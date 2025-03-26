import aes_keygen
import rsagen
import certificate_manager
import krl_manager

def main():
    while True:
        print("\nSecure Key Management System")
        print("1. Generate AES Key")
        print("2. Generate RSA Key Pair")
        print("3. Generate X.509 Certificate")
        print("4. Revoke Key")
        print("5. Check Key Revocation Status")
        print("6. Remove Key Revocation")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            aes_keygen.generate_aes_key()
        elif choice == "2":
            rsagen.generate_rsa_keys()
        elif choice == "3":
            certificate_manager.generate_x509_certificate()
        elif choice == "4":
            key_name = input("Enter key filename to revoke: ")
            krl_manager.revoke_key(key_name)
        elif choice == "5":
            key_name = input("Enter key filename to check: ")
            status = krl_manager.check_key_status(key_name)
            print(f"🔒 Key Revoked: {status}")
        elif choice == "6":
            key_name = input("Enter key filename to un-revoke: ")
            krl_manager.remove_key_revocation(key_name)
        elif choice == "7":
            break
        else:
            print("❌ Invalid Choice!")

if __name__ == "__main__":
    main()

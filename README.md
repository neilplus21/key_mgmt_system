# Secure Key Management System 

## Overview
The Secure Key Management System (KMS) is designed to handle cryptographic keys securely, ensuring proper key generation, storage, revocation, and authentication. It supports both symmetric and asymmetric encryption, with features such as key exchange, public key infrastructure (PKI), and key revocation management.

## Features
- **RSA Key Generation**: Generate private and public keys securely.
- **Key Revocation Management**: Maintain a Key Revocation List (KRL) to prevent the use of compromised keys.
- **Authentication & Signing**: Sign and verify messages using private and public keys.
- **Secure Key Storage**: Store keys safely in files with controlled access.
- **Key Revocation Handling**: Remove revoked keys from the system when generating new ones.
- **Diffie-Hellman Key Exchange**: Securely exchange keys between parties.
- **Public Key Infrastructure (PKI)**: Manage trusted keys effectively.

## Project Structure
```
Secure-KMS/
│── krl_manager.py         # Manages key revocation list (KRL)
│── rsagen.py              # Generates RSA key pairs
│── authentication.py      # Handles authentication & signing
│── main.py                # Main interface for system operations
│── krl.json               # Stores revoked key identifiers
│── README.md              # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `cryptography` library

### Install Dependencies
```sh
pip install cryptography
```

### Run the Main Application
```sh
python main.py
```

## Usage Guide
### 1. Generate RSA Keys
Run:
```sh
python rsagen.py
```
This generates `private_key.pem` and `public_key.pem`. It also ensures previously revoked keys are removed from the KRL.

### 2. Revoke a Key
Run:
```sh
python krl_manager.py
```
Enter the filename (e.g., `private_key.pem`) to revoke it.

### 3. Check Key Status
Use `check_key_status()` in `krl_manager.py` to determine if a key is revoked.

### 4. Sign and Verify Data
Modify `authentication.py` to sign and verify messages using:
```sh
python authentication.py
```

## Security Considerations
- **Protect Private Keys**: Store `private_key.pem` securely and limit access.
- **Use Strong Key Sizes**: Default RSA key size is 2048 bits for security.
- **Regularly Rotate Keys**: Periodically generate new keys to maintain security.
- **Monitor Revoked Keys**: Ensure revoked keys are not used accidentally.

## Future Enhancements
- Implement key expiration policies.
- Extend support for other encryption algorithms (AES, ECC).
- Improve key storage with hardware security modules (HSMs).

## License
This project is licensed under the MIT License.

## Contributors
- [Your Name] (Replace with your actual name or GitHub profile)


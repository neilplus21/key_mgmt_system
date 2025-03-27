# Secure Key Management System

## Overview
The Secure Key Management System (KMS) ensures secure cryptographic key handling, supporting symmetric and asymmetric encryption. It provides functionalities such as key generation, storage, exchange, revocation, and authentication, enhancing security and integrity in cryptographic operations.

## Features
- **AES & RSA Key Generation**: Securely generate symmetric and asymmetric keys.
- **Key Revocation Management**: Maintain a Key Revocation List (KRL) to track compromised keys.
- **Authentication & Signing**: Sign and verify messages using RSA private and public keys.
- **Diffie-Hellman Key Exchange**: Securely exchange keys between communicating parties.
- **Public Key Infrastructure (PKI)**: Manage trusted keys and X.509 certificates.
- **Secure Key Storage**: Ensure proper storage and controlled access to keys.

## Project Structure
```
Secure-KMS/
│── key_ex.py              # Handles Diffie-Hellman key exchange
│── aes_keygen.py          # Generates AES keys
│── rsagen.py              # Generates RSA key pairs
│── certificate_manager.py # Manages X.509 certificates
│── krl_manager.py         # Handles key revocation
│── authentication.py      # Manages authentication & signing
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
### 1. Generate AES and RSA Keys
Run:
```sh
python aes_keygen.py
python rsagen.py
```
This generates `aes_key.bin`, `private_key.pem`, and `public_key.pem`, ensuring revoked keys are removed.

### 2. Revoke a Key
Run:
```sh
python krl_manager.py
```
Enter the filename (e.g., `private_key.pem`) to revoke it.

### 3. Check Key Revocation Status
Use `check_key_status()` in `krl_manager.py` to determine if a key is revoked.

### 4. Sign and Verify Data
Modify `authentication.py` to sign and verify messages using:
```sh
python authentication.py
```

### 5. Perform Diffie-Hellman Key Exchange
Generate a Diffie-Hellman key pair:
```sh
python key_ex.py
```
Compute a shared secret using a peer's public key:
```sh
python key_ex.py compute_shared_secret peer_public_key.pem
```

## Security Considerations
- **Protect Private Keys**: Store `private_key.pem` securely and restrict access.
- **Use Strong Key Sizes**: Default RSA key size is 2048 bits for enhanced security.
- **Regular Key Rotation**: Periodically generate new keys to maintain security.
- **Monitor Revoked Keys**: Ensure revoked keys are not used accidentally.


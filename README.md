# Password Manager

A simple and secure password manager built with Python. This application allows users to securely store and retrieve account credentials using encryption and hashing techniques.

## Features

- **Master Password**: Protect your account credentials with a master password.
- **Password Encryption**: All stored passwords are encrypted using the `Fernet` module from the `cryptography` library.
- **Secure Master Password Storage**: Master password is securely hashed using the `bcrypt` algorithm.
- **Add and Retrieve Accounts**: Save new account credentials and retrieve them when needed.

## Prerequisites

- Python 3.6 or above
- The following Python libraries:
  - `bcrypt`
  - `cryptography`


# **Usage**

Add an Account
Select the [1] Add Account option.
Enter the account name, username, and password.
The account is securely saved.

Retrieve an Account
Select the [2] Retrieve Account option.
Enter the account name.
The stored username and decrypted password are displayed.

Exit
Select [3] Exit to close the application.

# **File Structure**

password_manager.py: Main script for the application.

key.key: File containing the encryption key. Automatically generated.

master.hash: File containing the hashed master password. Automatically generated.

passwords.json: File where encrypted account credentials are stored.

# Security Notes

Encryption Key: The encryption key is stored locally in key.key. Keep this file secure to prevent unauthorized access.

Master Password: The master password is securely hashed and stored locally in master.hash.

Account Passwords: All account passwords are encrypted before storage and decrypted only when retrieved.

# **Acknowledgments**
bcrypt for secure password hashing.
cryptography for encryption utilities.

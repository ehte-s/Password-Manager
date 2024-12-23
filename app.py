import json
import bcrypt
from cryptography.fernet import Fernet
import os

# Generate or load encryption key
KEY_FILE = "key.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as key_file:
    FERNET_KEY = key_file.read()

cipher = Fernet(FERNET_KEY)
PASSWORD_DB = "passwords.json"

def hash_master_password(master_password):
    return bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())

def verify_master_password(master_password, hashed_password):
    return bcrypt.checkpw(master_password.encode(), hashed_password)

def load_passwords():
    if not os.path.exists(PASSWORD_DB):
        return {"accounts": []}
    with open(PASSWORD_DB, "r") as file:
        return json.load(file)

def save_passwords(data):
    with open(PASSWORD_DB, "w") as file:
        json.dump(data, file, indent=4)

def add_account(name, username, password):
    data = load_passwords()
    encrypted_password = cipher.encrypt(password.encode())
    data["accounts"].append({
        "name": name,
        "username": username,
        "password": encrypted_password.decode()
    })
    save_passwords(data)

def retrieve_account(name):
    data = load_passwords()
    for account in data["accounts"]:
        if account["name"].lower() == name.lower():
            decrypted_password = cipher.decrypt(account["password"].encode()).decode()
            return account["username"], decrypted_password
    return None, None

if __name__ == "__main__":
    print("Welcome to Password Manager!")
    master_password = input("Enter your master password: ")

    # Load or create master password
    if not os.path.exists("master.hash"):
        print("Setting up a new master password...")
        hashed = hash_master_password(master_password)
        with open("master.hash", "wb") as file:
            file.write(hashed)
    else:
        with open("master.hash", "rb") as file:
            hashed = file.read()
        if not verify_master_password(master_password, hashed):
            print("Invalid master password!")
            exit()

    while True:
        print("\nOptions: [1] Add Account [2] Retrieve Account [3] Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Account Name: ")
            username = input("Username: ")
            password = input("Password: ")
            add_account(name, username, password)
            print(f"Account '{name}' added successfully!")
        elif choice == "2":
            name = input("Account Name to Retrieve: ")
            username, password = retrieve_account(name)
            if username:
                print(f"Username: {username}\nPassword: {password}")
            else:
                print(f"No account found with name '{name}'.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

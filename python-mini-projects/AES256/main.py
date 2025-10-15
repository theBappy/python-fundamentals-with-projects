import hashlib
from base64 import b64decode, b64encode
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def encrypt(plain_text, password):
    if not password:
        raise ValueError("Password cannot be empty.")
    salt = get_random_bytes(AES.block_size)
    private_key = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
        dklen=32
    )
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, "utf-8"))
    return {
        "cipher_text":b64encode(cipher_text).decode("utf-8"),
        "salt": b64encode(salt).decode("utf-8"),
        "nonce": b64encode(cipher_config.nonce).decode("utf-8"),
        "tag": b64encode(tag).decode("utf-8")
    }

def decrypt(enc_dict, password):
    if not password:
        raise ValueError("Password cannot be empty.")
    try:
        salt = b64decode(enc_dict["salt"])
        cipher_text = b64decode(enc_dict["cipher_text"])
        nonce = b64decode(enc_dict["nonce"])
        tag = b64decode(enc_dict["tag"])
        private_key = hashlib.scrypt(
            password.encode(),
            salt=salt,
            n=2**14,
            r=8,
            p=1,
            dklen=32
        )
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode("utf-8")
    except (ValueError, KeyError) as e:
        raise ValueError("Invalid encrypted message format.") from e
    
def main():
    print("\t\tAES 256 Encryption and Decryption Algorithm")
    print("\t\t-------------------------------------------\n\n")
    x = input("Enter 1 to encrypt and 2 to decrypt: ")
    if x == "1":
        password = input("Enter the password: ")
        secret_msg = input("\nEnter the secret message: ")

        encrypted = encrypt(secret_msg, password)
        print("\n\nEncrypted: ")
        print("-----------\n")
        for k, v in encrypted.items():
            print(f"{k}: {v}")

    elif x == "2":
        try:
            encrypted = {}
            encrypted["cipher_text"] = input("Enter the cipher text: ")
            encrypted["salt"] = input("Enter the salt: ")
            encrypted["nonce"] = input("Enter the nonce: ")
            encrypted["tag"] = input("Enter the tag: ")

            decrypted = decrypt(encrypted, password)
            print("\n\nDecrypted")
            print("---------------\n")
            print(decrypted)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()


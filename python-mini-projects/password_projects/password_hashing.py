import argparse
import hashlib

parser = argparse.ArgumentParser(description="hashing given password")
parser.add_argument("password", help="input password you want to hash")
parser.add_argument(
    "-t", "--type", default="sha256",
    choices=["sha256", "md5", "sha512", "sha1"]
)

args = parser.parse_args()

password = args.password
hash_type = args.type

m = getattr(hashlib, hash_type)()
m.update(password.encode())

print("< has-type : " + hash_type + " >")

print(m.hexdigest())
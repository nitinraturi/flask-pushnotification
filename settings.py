from solidwebpush import Pusher
import os

# DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"vapid","private_key.txt")
# DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"vapid","public_key.txt")
#
#
# print("private_key",DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH)
# print("public_key",DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH)
# VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
# VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

def generate_public_key():
    pusher = Pusher()
    key = pusher.getB64PublicKey()
    print("public key",key)
    return key

def save_key_file():
    path = os.path.join(BASE_DIR,"vapid","public_key.txt")
    key = generate_public_key()
    with open(path,'w') as f:
        f.write(key)


if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    save_key_file()

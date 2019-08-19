import os

DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")

VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

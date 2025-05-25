import hashlib

# Simulasi penyimpanan password menggunakan MD5 (TIDAK AMAN)
def store_password_md5(password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    print("Password disimpan (MD5):", hashed)
    return hashed

store_password_md5("Telkom12345!")

import hashlib
import os

# Simulasi penyimpanan password menggunakan PBKDF2 (AMAN)
def store_password_pbkdf2(password):
    salt = os.urandom(16)  # salt acak
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    print("Password disimpan (PBKDF2):", hashed.hex())
    return salt, hashed

store_password_pbkdf2("Telkom12345!")

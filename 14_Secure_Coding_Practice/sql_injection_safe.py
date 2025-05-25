# cwe89_safe.py

import sqlite3

# Setup awal database (sekali saja)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
conn.commit()

# Ambil input dari user
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# ✅ Gunakan parameterized query untuk mencegah injeksi
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

# Cek apakah login berhasil
result = cursor.fetchone()
if result:
    print("Login berhasil sebagai:", result[0])
else:
    print("Login gagal.")

conn.close()
# xss_safe.py

import html  # Modul bawaan untuk escape karakter HTML

user_input = input("Masukkan nama Anda: ")

# ✅ Escape karakter spesial sebelum dimasukkan ke HTML
escaped_input = html.escape(user_input)

html_content = f"""
<html>
    <head><title>Selamat Datang</title></head>
    <body>
        <h1>Halo, {escaped_input}</h1>
    </body>
</html>
"""

with open("output_safe.html", "w") as file:
    file.write(html_content)

print("File HTML aman telah dibuat: output_safe.html")
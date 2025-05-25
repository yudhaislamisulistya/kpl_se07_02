# xss_vulnerable.py

user_input = input("Masukkan nama Anda: ")

# ❌ Rentan: input langsung dimasukkan ke HTML tanpa disanitasi
html = f"""
<html>
    <head><title>Selamat Datang</title></head>
    <body>
        <h1>Halo, {user_input}</h1>
    </body>
</html>
"""

with open("output.html", "w") as file:
    file.write(html)

print("File HTML telah dibuat: output.html")
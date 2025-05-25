# Contoh Salah
def divide(a, b):
    try:
        result = a / b
    except:
        print("Terjadi kesalahan!")
        result = 0
    return result

print(divide(10, 0))


# Contoh Benar
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol.")
        result = 0
    except TypeError:
        print("Tipe data tidak valid. Masukkan angka.")
        result = 0
    return result

print(divide(10, 0))        # Output: Tidak bisa membagi dengan nol.
print(divide(10, "dua"))    # Output: Tipe data tidak valid. Masukkan angka.

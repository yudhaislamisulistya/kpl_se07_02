# from config_env import get_base_url
from config_json import get_base_url

import requests

def main():
    base_url = get_base_url()
    print("Base URL:", base_url)
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            print("Koneksi Berhasil")
        else:
            print("Koneksi Gagal")
    except Exception as e:
        print(f"Koneksi Gagal: {e}")
        
if __name__ == "__main__":
    main()
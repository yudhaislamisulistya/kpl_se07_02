import json

ip_address = "192.168.1.33" # IP address of the device

with open("config.json", "r") as file:
    config = json.load(file)
    ip_address = config["IP_SERVER"]
    
print(f"IP address from config: {ip_address}")
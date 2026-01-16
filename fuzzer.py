import socket
import random
import string
import time
import sys

print("=========================================")
print("Incremental Socket Fuzzer")
print("=========================================")

if len(sys.argv) != 5:
    print("Usage: python socket_fuzzer.py <ip> <port> <start_size> <step>")
    sys.exit(1)

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
payload_length = int(sys.argv[3])
step = int(sys.argv[4])

def generate_payload(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))

while True:
    try:
        payload = generate_payload(payload_length)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(payload.encode())
        s.close()

        print(f"Sent payload of size: {payload_length}")

        payload_length += step
        time.sleep(0.5)

    except:
        print("[!!!] CRASH DETECTED")
        print("Payload size:", payload_length)
        print("Payload used:", payload)
        break

print("\n=========================================")
print("Developed by sudo_0xksh")
print("=========================================")

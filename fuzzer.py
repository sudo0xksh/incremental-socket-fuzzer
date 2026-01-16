import socket
import random
import string
import time

target_ip = "127.0.0.1"
target_port = 9999

def generate_payload(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))

payload_length = 100

while True:
    try:
        payload = generate_payload(payload_length)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(payload.encode())
        s.close()

        print(f"Sent payload of size: {payload_length}")

        payload_length += 100
        time.sleep(0.5)

    except:
        print("[!!!] CRASH DETECTED")
        print("Payload size:", payload_length)
        print("Payload used:", payload)
        break

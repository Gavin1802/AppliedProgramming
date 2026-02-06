import socket
import os

HOST = '127.0.0.1'
PORT = 65432
CLIENT_FOLDER = 'client_data'

if not os.path.exists(CLIENT_FOLDER):
    os.makedirs(CLIENT_FOLDER)


def send_file(s, filename):
    # (Same as Phase 3 - keep this logic!)
    filepath = os.path.join(CLIENT_FOLDER, filename)
    if not os.path.exists(filepath):
        print("File not found.")
        return

    s.sendall(f"SAVE {filename}".encode('utf-8'))
    s.recv(1024)  # Wait for READY

    file_size = os.path.getsize(filepath)
    s.sendall(str(file_size).encode('utf-8'))
    s.recv(1024)  # Wait for READY

    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk: break
            s.sendall(chunk)

    print(f"Server: {s.recv(1024).decode('utf-8')}")


def download_file(s, filename):
    # 1. Send Request
    s.sendall(f"READ {filename}".encode('utf-8'))

    # 2. Check Server Response
    response = s.recv(1024).decode('utf-8')

    if response == "ERROR_NO_FILE":
        print(f"Server says: File '{filename}' does not exist.")
        return

    if response.startswith("EXISTS"):
        # Parse size from "EXISTS 1024"
        _, size_str = response.split(' ')
        file_size = int(size_str)

        # 3. Tell server we are ready
        s.sendall(b"OK_SEND_IT")

        # 4. Receive Data
        filepath = os.path.join(CLIENT_FOLDER, f"downloaded_{filename}")
        received = 0
        print(f"Downloading {filename} ({file_size} bytes)...")

        with open(filepath, 'wb') as f:
            while received < file_size:
                chunk = s.recv(1024)
                if not chunk: break
                f.write(chunk)
                received += len(chunk)

        print(f"Saved to {filepath}")


print("--- Client Running (Phase 4) ---")
# ... Main setup ...
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        u_in = input("Vault> ").strip()
        parts = u_in.split(' ')
        cmd = parts[0].upper()

        if cmd == 'SAVE':
            if len(parts) > 1: send_file(s, parts[1])
        elif cmd == 'READ':
            if len(parts) > 1: download_file(s, parts[1])
        elif cmd == 'EXIT':
            s.sendall(b"EXIT")
            break
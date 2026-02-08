import socket
import os

# Configuration
HOST = '127.0.0.1'  # Localhost (VM forwarding)
PORT = 65432
CLIENT_FOLDER = 'client_data'

# Ensure storage folder
if not os.path.exists(CLIENT_FOLDER):
    os.makedirs(CLIENT_FOLDER)


def send_file(s, filename):
    """Uploads file to server."""
    filepath = os.path.join(CLIENT_FOLDER, filename)

    # Verify local file exists
    if not os.path.exists(filepath):
        print("File not found.")
        return

    # Send SAVE command
    s.sendall(f"SAVE {filename}".encode('utf-8'))
    s.recv(1024)  # Wait for READY

    # Send file size
    file_size = os.path.getsize(filepath)
    s.sendall(str(file_size).encode('utf-8'))
    s.recv(1024)  # Wait for READY

    # Stream file chunks
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk: break
            s.sendall(chunk)

    # Wait for confirmation
    print(f"Server: {s.recv(1024).decode('utf-8')}")


def download_file(s, filename):
    """Downloads file from server."""
    # Send READ command
    s.sendall(f"READ {filename}".encode('utf-8'))

    # Check server response
    response = s.recv(1024).decode('utf-8')

    if response == "ERROR_NO_FILE":
        print(f"Server says: File '{filename}' does not exist.")
        return

    if response.startswith("EXISTS"):
        # Parse file size
        _, size_str = response.split(' ')
        file_size = int(size_str)

        # Request stream start
        s.sendall(b"OK_SEND_IT")

        # Write incoming chunks
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
# Connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Command loop
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
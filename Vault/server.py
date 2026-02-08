import socket
import os

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432
SERVER_FOLDER = 'server_data'

# Ensure storage folder
if not os.path.exists(SERVER_FOLDER):
    os.makedirs(SERVER_FOLDER)


def receive_file(conn, filename):
    """Handles file uploads."""
    # Acknowledge and get size
    conn.sendall(b"READY_FOR_SIZE")
    file_size = int(conn.recv(1024).decode('utf-8'))
    conn.sendall(b"READY_FOR_DATA")

    filepath = os.path.join(SERVER_FOLDER, filename)
    received_bytes = 0

    # Receive exact bytes
    with open(filepath, 'wb') as f:
        while received_bytes < file_size:
            chunk = conn.recv(1024)
            if not chunk: break
            f.write(chunk)
            received_bytes += len(chunk)

    print(f"File {filename} received.")
    conn.sendall(b"UPLOAD_COMPLETE")


def send_file_to_client(conn, filename):
    """Handles file downloads."""
    filepath = os.path.join(SERVER_FOLDER, filename)

    # Check existence
    if not os.path.exists(filepath):
        conn.sendall(b"ERROR_NO_FILE")
        return

    # Send existence and size
    file_size = os.path.getsize(filepath)
    conn.sendall(f"EXISTS {file_size}".encode('utf-8'))

    # Wait for client
    response = conn.recv(1024)
    if response.decode('utf-8') != 'OK_SEND_IT':
        return

    # Stream file
    print(f"Sending {filename} to client...")
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk: break
            conn.sendall(chunk)

    print("File sent successfully.")


print("--- Vault Server Running (Phase 4) ---")
# Start server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}...")

    # Accept connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # Main loop
        while True:
            data = conn.recv(1024)
            if not data: break

            # Parse command
            parts = data.decode('utf-8').strip().split(' ')
            cmd = parts[0].upper()

            # Execute command
            if cmd == 'SAVE':
                receive_file(conn, parts[1])
            elif cmd == 'READ':
                send_file_to_client(conn, parts[1])
            elif cmd == 'EXIT':
                break
            else:
                conn.sendall(b"UNKNOWN_COMMAND")
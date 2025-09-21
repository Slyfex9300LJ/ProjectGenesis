# The server side.
# server.py
import socket


def run_server():
    host = '127.0.0.1'  # localhost
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("Server listening...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                message = "Hello from server!"
                conn.sendall(message.encode())

                # Send a message to the client.
    except socket.error as e:
        print(f"Server error: {e}")  # Basic error handling for network operations.


# The client side.
# client.py
import socket


def run_client():
    host = '127.0.0.1'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")  # Receive the message from the server[cite: 31].
    except socket.error as e:
        print(f"Client error: {e}")  # Basic error handling for network operations.

# To run: start the server in one terminal and the client in another.
# For demonstration purposes, both functions are here.
# run_server()
# run_client()
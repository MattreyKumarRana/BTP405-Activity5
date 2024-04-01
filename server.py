# Name      :       Mattrey Kumar Rana
# Email     :       mrana23@myseneca.ca
# Student ID:       116092222

import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode('utf-8')
        print(f"Received message: {message}")

        # Echo the message back to the client
        client_socket.sendall(data)

        if message.lower() == 'quit':
            break

    client_socket.close()

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 65432

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connected to {client_address}")

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    main()

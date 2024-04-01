# Name      :       Mattrey Kumar Rana
# Email     :       mrana23@myseneca.ca
# Student ID:       116092222

import socket

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 65432

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((host, port))

        while True:
            # Prompt the user for a message
            message = input("Enter message to send (type 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            # Send the message to the server
            client_socket.sendall(message.encode('utf-8'))

            # Receive the response from the server
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")

if __name__ == "__main__":
    main()

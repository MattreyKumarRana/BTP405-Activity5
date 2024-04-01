# Concurrent Echo Server in Python

This project implements a concurrent echo server in Python, capable of handling multiple client connections simultaneously. The server listens for incoming connections, echoes back any messages it receives from clients, and can handle a special "quit" message to close a client connection.

## Server (server.py)

To run the server, execute the `server.py` script. The server will listen on `localhost` and port `65432` by default. You can change the host and port in the script if needed.

## Client (client.py)

To run the client, execute the `client.py` script. The client will connect to the server using TCP and allow you to send messages to the server. Type "quit" to exit the client.

## Usage

1. Start the server by running `server.py`.
2. Run multiple instances of the client (`client.py`) to simulate multiple clients connecting to the server.
3. Send messages from the clients and observe the echo responses from the server.
4. Type "quit" in a client to close its connection with the server.

## Example

```bash
$ python server.py
Server listening on 127.0.0.1:65432

$ python client.py
Enter message to send (type 'quit' to exit): Hello, server!
Received from server: Hello, server!

$ python client.py
Enter message to send (type 'quit' to exit): quit
```

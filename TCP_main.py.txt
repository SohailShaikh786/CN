import socket

def tcp_server():
    # Define server address and port
    server_address = "127.0.0.1"  # Localhost
    server_port = 65432  # Port to listen on

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((server_address, server_port))
        server_socket.listen()  # Start listening for connections
        print(f"Server is listening on {server_address}:{server_port}")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break  # Break if the connection is closed

                    # Decode and print the received message
                    message = data.decode()
                    print(f"Received from client: {message}")

                    # Send an acknowledgment back to the client
                    response = f"Server received: {message}"
                    client_socket.sendall(response.encode())

if __name__ == "__main__":
    tcp_server()

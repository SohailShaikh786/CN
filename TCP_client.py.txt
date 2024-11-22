import socket

def tcp_client():
    # Define server address and port
    server_address = "127.0.0.1"  # Localhost
    server_port = 65432           # Port the server is listening on

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        print(f"Connected to server at {server_address}:{server_port}")

        while True:
            # Take user input
            message = input("Enter message to send to server (or 'exit' to quit): ")
            if message.lower() == "exit":
                print("Exiting client.")
                break

            # Send the input message to the server
            client_socket.sendall(message.encode())
            print(f"Sent to server: {message}")

            # Receive response from the server
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    tcp_client()

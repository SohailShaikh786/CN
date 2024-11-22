import socket

def udp_client():
    # Define server address and port
    server_address = "127.0.0.1"  # Localhost
    server_port = 65432           # Port the server is listening on

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            # Take user input
            message = input("Enter message to send to server (or 'exit' to quit): ")
            if message.lower() == "exit":
                print("Exiting client.")
                break

            # Send the input message to the server
            client_socket.sendto(message.encode(), (server_address, server_port))
            print(f"Sent to server: {message}")

            # Receive response from the server
            data, server = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    udp_client()

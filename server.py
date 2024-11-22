import socket
import json

def selection_sort_steps(arr):
    steps = []
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            # Save the current array state and highlighted indexes
            steps.append((arr[:], i, j, min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # Save the state after swapping
        steps.append((arr[:], i, min_index, min_index))
    return steps

def main():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Server is listening...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode()
                if data:
                    arr = list(map(int, data.split(',')))
                    print(f"Received array: {arr}")

                    # Perform selection sort and capture steps
                    steps = selection_sort_steps(arr)

                    # Send the steps as JSON to the client
                    conn.sendall(json.dumps(steps).encode())

if __name__ == "__main__":
    main()

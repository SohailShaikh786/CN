import socket
import json
import tkinter as tk
import time

def visualize_sorting(steps):
    for step in steps:
        arr, i, j, min_index = step
        draw_array(arr, i, j, min_index)
        root.update_idletasks()
        time.sleep(0.5)

def draw_array(arr, i, j, min_index):
    canvas.delete("all")
    c_width = canvas.winfo_width()
    c_height = canvas.winfo_height()
    bar_width = c_width / len(arr)
    max_value = max(arr)

    for k, val in enumerate(arr):
        x0 = k * bar_width
        y0 = c_height - (val / max_value) * c_height
        x1 = (k + 1) * bar_width
        y1 = c_height

        color = "grey"
        if k == i:
            color = "blue"  # Current index
        elif k == j:
            color = "red"   # Comparing index
        elif k == min_index:
            color = "green" # Minimum index

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0 + bar_width / 2, y0, anchor=tk.S, text=str(val))

def send_array():
    array_str = entry.get()
    try:
        array = list(map(int, array_str.split(',')))
    except ValueError:
        tk.messagebox.showerror("Invalid input", "Please enter a comma-separated list of numbers.")
        return

    server_ip = '127.0.0.1'
    server_port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(array_str.encode())

        # Receive the sorting steps from the server
        steps_data = client_socket.recv(4096).decode()
        steps = json.loads(steps_data)

        # Visualize sorting process
        visualize_sorting(steps)

# GUI setup
root = tk.Tk()
root.title("Selection Sort Visualization")

# Input and button frame
frame = tk.Frame(root)
frame.pack(pady=10)

input_label = tk.Label(frame, text="Enter a list of numbers (comma-separated):")
input_label.grid(row=0, column=0, padx=5)
entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)
submit_button = tk.Button(frame, text="Sort Array", command=send_array)
submit_button.grid(row=0, column=2, padx=5)

# Canvas for drawing the array
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)

root.mainloop()

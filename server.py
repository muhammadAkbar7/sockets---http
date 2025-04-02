# Citation for the following code
# Date: 01/26/25
# Adopted/modifed/based code on:
# https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python, https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/
# https://globaldev.tech/blog/working-tcp-sockets, https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'  # localhost address
PORT = 8001  # Port number

# Given HTTP response data
data = "HTTP/1.1 200 OK\r\n"\
       "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
       "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Bind the socket to the address and port
    server_socket.listen()  # Listens for any connections
    print(f"Server running on http://{HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")  # Print client connection details
    # Reads the request from the client
    request = conn.recv(1024)  # Read up to 1024 bytes
    print("Received:")
    print(request)  # Print the raw request data
    
    # Prints outgoing response
    print("Sending>>>>>>>>")
    print(data)
    print("<<<<<<<<")
    
    # Sends the HTTP response
    conn.sendall(data.encode())
    # Closes the connection
    conn.close()

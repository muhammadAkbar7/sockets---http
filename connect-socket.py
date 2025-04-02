# Citation for the following code
# Date: 01/26/25
# Adopted/modifed/based code on:
# https://www.pubnub.com/blog/python-socket-programming-client-server/

import socket

host = "gaia.cs.umass.edu"  # Server hostname
port = 80  # Server port

# Creating the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((host, port))

# Sent an HTTP GET request 
client.send("GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n".encode())

# Receiving the response from the server
from_server = client.recv(4096)

# Closed the connection
client.close()

# Printed the server's response
print(from_server.decode())


# Citation for the following code
# Date: 01/26/25
# Adopted/modifed/based code on:
# https://realpython.com/python-sockets/, https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str, https://docs.python.org/3/library/socket.html#socket.socket.recv 

import socket

host = "gaia.cs.umass.edu"  # Server hostname
port = 80  # Server port
request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n" # given request

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connects to the server
    s.connect((host, port))
    
    # Sends the GET request
    s.sendall(request.encode())
    
    # Initialize a response to hold all the bytes
    response = b""
    
    # While there are still bytes, breaks it into chunks (because it's a large file)
    while True:
        chunk = s.recv(4096)  # Read up to 4096 bytes at a time
        if len(chunk) <= 0:  # If there are no bytes left, it will exit
            break
        response += chunk  # Append the bytes to the responses

# Decodes and prints the response
decoded_response = response.decode()
print(decoded_response)

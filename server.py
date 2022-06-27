import socket
from _thread import *
import sys

from pyrsistent import b

server = "192.168.254.15"  # Server string
port = 5555  # Port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET refers to the address-family ipv4.
#  The SOCK_STREAM means connection-oriented TCP protocol.

try:
    s.bind((server, port))  # Try to bind the server to the port.

except socket.error as e:  # If unsuccessful throw socket error.
    str(e)

s.listen(2)  # It starts listening for incommiing connections. Max clients is 2.
print("Server Started, Waiting for Connections...")


def threaded_client(connection):
    connection.send(str.encode("Connected")) # Send Messsage
    reply = ""
    while True:
        try:
            data = connection.recv(1024)  # Attempt to recieve data from the client.
            reply = data.decode("utf-8")  # Decode the data.

            if not data:
                print("Disconnected")  # If no data is recieved, print disconnected.
                break
            else:
                print("Received: ", reply)  # Else, print received data.
                print("Sending: ", reply)   # Print sending data

            connection.sendall(str.encode(reply))
        except:
            break
    
    print("Lost Connection")
    connection.close()


while True:
    connection, address = s.accept()  # Establish connection with client.
    print("Connected to: ", address)

    start_new_thread(threaded_client, (connection,))  # Create a new thread for each client.
    #  This way multiple clients can connect at the same time.

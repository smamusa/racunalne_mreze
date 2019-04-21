'''
Prvi kod

import socket
import sys

server_address = ('localhost', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
	print('Server is listening')
	data, address = sock.recvfrom(4096)
	if data:
		sent = sock.sendto(data, address)

'''

# Drugi kod

import sys
from socket import *

print (sys.argv[0])
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

serverSocket= socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName,serverPort))
print("The server is ready to receive\n")

while True:
	message, clientAddress= serverSocket.recvfrom(2048)
	modifiedMessage= message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)
'''
Prvi kod

import socket
import sys

server_address = ('127.0.0.1', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messsage = input('Unesi poruku za slanje')

#exception handling sistem

try:
	sent = sock.sendto(messsage.encode(), server_address)
	data, server = sock.recvfrom(4096)
finally:
	sock.close()

'''

# Drugi kod

import sys
from socket import *

serverName= sys.argv[1]
serverPort= int(sys.argv[2])

clientSocket= socket(AF_INET, SOCK_DGRAM)
message= input('Input lowercase sentence:\n')
clientSocket.sendto(message.encode(), (serverName,serverPort))
modifiedMessage, serverAddress= clientSocket.recvfrom(2048)
print('Server returned message: ',modifiedMessage.decode())
clientSocket.close()
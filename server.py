#coding=UTF-8

'''
server test
'''

import socket
import threading

bind_ip="127.0.0.1"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print("Listen on",bind_ip,":",bind_port)
'''
def handle_client( client_socket)
    request=client_socket.recv(1024)
    print("Received:",request)

    client_socket.
'''
while True:
    (clint,addr)=server.accept()
    print("client info:",clint,addr)
    msg=clint.recv(1024)
    if not msg:
        pass
    else:
        print("Client send:",msg)
        clint.send("Hello I'm server".encode('utf-8'))
    clint.close
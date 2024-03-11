import socket

from _thread import *
import threading

# Server settings

HOST = '127.0.0.1' 
PORT = 12345

lock = threading.Lock()

def clientThread(clientSocket):
    lock.acquire()
    
    while True:
        data = clientSocket.recv(1024)
        if not data:
            print('Bye')
            
            lock.release()
            break
        
        data = data[::-1]
        
        c.send(data)
        
    c.close()

def Main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverSocket.bind((HOST, PORT))
    
    serverSocket.listen(5)
    
    while True:
        (clientSocket, address) = serverSocket.accept()
        
        conn = clientThread(clientSocket)
        


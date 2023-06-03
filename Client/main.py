from Client.client import Client
import socket

clientObj = Client(socket.AF_INET, socket.SOCK_STREAM,"localhost",9091)
print("Hello to the chat application")
print("Enter your Message !!")
message = input(" >>> ")
clientObj.sendall(message.encode())
while True:
    message = input(" >>> ")
    try:
        clientObj.sendall(message.encode())
        data = clientObj.recv(1024).decode() 
        while clientObj.recv(1024).decode() != "\0":
            data += clientObj.recv(1024).decode()
    except Exception as e:
        clientObj.close()
        break
from Client.client import Client
import socket

clientObj = Client(socket.AF_INET, socket.SOCK_STREAM,"localhost",9091)
print("Hello to the chat application")
print("Enter your Message !!")
while True:
    message = input(" >>> ")
    try:
        clientObj.sendall(message.encode())
        print(clientObj.recv(1024).decode())
    except Exception as e:
        print(e)
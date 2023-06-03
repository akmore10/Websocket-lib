import socket
from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
from DataStore.Database import Database,Message

class WebSocketRequestHandler(BaseRequestHandler):
    database = Database()

    def __init__(self,request:socket.socket, client_address:tuple, server:ThreadingTCPServer):
        super().__init__(request,client_address,server)
        self.clientName = ""
        self.currentIndx = 0
        
    def setup(self) -> None:
        """
            Here I can write the code to get the all the current messages transfered in the
            group chat or authentication can be done before exceptions can be raised.
        """
        self.clientName = self.request.recv(1024).decode()
        
    def handle(self) -> None:
        """
            Here Sending new chats with each other
        """
        while True:
            try:
                data = self.request.recv(1024).decode()
                if data == "exit":
                    self.finish()
                    break
                # Process received data
                WebSocketRequestHandler.database.insert(Message(self.clientName,data))
                message : Message = WebSocketRequestHandler.database.getAll()
            
                for m in message:
                    print(m)
                    self.request.sendall(m.__str__().encode())
                
            except Exception:
                print("Client connection timed out")
                break
    
    def finish(self) -> None:
        """
            Here when the client connection can be closed as we have the clientSocket .
        """
        self.request.close()

class Messages:
    def __init__(self,message , clientName):
        self.messsage = message
        self.clientAddress = clientName
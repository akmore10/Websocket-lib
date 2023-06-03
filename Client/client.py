import socket


class Client(socket.socket):
    def __init__(self,socket_type : socket.AddressFamily, sock_stream:socket.SocketKind, server_address : str,server_port :int):
        super().__init__(socket_type , sock_stream)
        self.server_address = server_address
        self.server_port = server_port
        self.connect((self.server_address,self.server_port))
    
    def close(self):
        self.close()


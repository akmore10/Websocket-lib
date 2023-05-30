from socketserver import ThreadingTCPServer
from Server.requestHandler import WebSocketRequestHandler

webSocketServer = ThreadingTCPServer(("localhost",9091),WebSocketRequestHandler)
webSocketServer.serve_forever()
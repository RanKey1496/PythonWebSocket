from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import sys

port = 8095

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', port, SimpleEcho)
server.serveforever()
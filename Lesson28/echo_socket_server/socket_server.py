from socketserver import BaseRequestHandler, TCPServer


SERVER_HOST = ('127.0.0.1', 9000)


class EchoRequestHandler(BaseRequestHandler):
    BUFF_SIZE: int = 1024

    def handle(self) -> None:
        while True:
            data = self.request.recv(self.BUFF_SIZE)
            self.request.sendall(data)
            if not data:
                break


if __name__ == '__main__':
    server = TCPServer(SERVER_HOST, EchoRequestHandler)
    server.serve_forever()

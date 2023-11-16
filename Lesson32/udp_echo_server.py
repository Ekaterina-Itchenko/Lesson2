from socketserver import BaseRequestHandler, UDPServer
from dataclasses import dataclass


@dataclass
class ServerConfig:
    addr: str
    port: int


class ServerRequestHandler(BaseRequestHandler):
    def handle(self) -> None:
        data = self.request[0]
        print(data.decode())
        sock = self.request[1]
        sock.sendto(data.encode(), self.client_address)


if __name__ == '__main__':
    server_addr = ServerConfig(addr='127.0.0.1', port=8000)
    HOST, PORT = server_addr.addr, server_addr.port
    dns_server = UDPServer((HOST, PORT), ServerRequestHandler)
    dns_server.serve_forever()

import socket
from dataclasses import dataclass
import random


@dataclass
class DNSConfig:
    host: str
    port: int


@dataclass
class DNSHeader:
    ID: str = "{:04x}".format(random.choice(range(65536)))
    QR: str = '0'
    OPCODE: str = '0'.zfill(4)
    AA: str = '0'
    TC: str = '0'
    RD: str = '1'
    RA: str = '0'
    Z: str = '0'.zfill(3)
    RCODE: str = '0'.zfill(4)
    QDCOUNT: str = "{:04x}".format(1)
    ANSCOUNT: str = "{:04x}".format(0)
    NSCOUNT: str = "{:04x}".format(0)
    ARCOUNT: str = "{:04x}".format(0)

    def __str__(self) -> str:
        return (self.ID + self._get_flags() + self.QDCOUNT +
                self.ANSCOUNT + self.NSCOUNT + self.ARCOUNT)

    def _get_flags(self) -> str:
        flags_params = (self.QR + self.OPCODE + self.AA +
                        self.TC + self.RD + self.RA + self.Z + self.RCODE)
        return "{:04x}".format(int(flags_params, 2))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == "__main__":
    server_addr = DNSConfig(host='8.8.8.8', port=53)
    while True:
        choice = input('1 - Get IP;\n2 - Exit;\nYour choice: ')
        if choice == '2':
            break
        elif choice == '1':
            domain_name = input("Enter domain name: ")
            sock.sendto(domain_name.encode(),
                        (server_addr.host, server_addr.port))
            data = sock.recv(1024)
            print(data.decode())

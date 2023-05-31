import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.bind(('127.0.0.1', 5001))
server.listen()


while True:
    print('Server is ready for connection.')
    client, address = server.accept()
    print(f"Server connected with {address}")
    while True:
        BUFF_SIZE = 16
        message = bytes()
        while True:
            data = client.recv(BUFF_SIZE)
            message += data
            if len(data) < BUFF_SIZE:
                break
        print(f"Recieved message: {message}.")
        client.sendall(message)
        if not data:
            break

server.close()

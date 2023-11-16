import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 5001))
while True:
    answer = int(input('1 - send message;\n2 - exit\nYour choice: '))
    if answer == 2:
        break
    if answer == 1:
        data = input('Enter a message: ').encode()
        sock.sendall(data)
        response = bytes()
        BUFF_SIZE = 8
        while True:
            message = sock.recv(BUFF_SIZE)
            response += message
            if len(message) < BUFF_SIZE:
                break
        print(response.decode())

sock.close()

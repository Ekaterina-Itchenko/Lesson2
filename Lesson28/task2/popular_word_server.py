import socket
from random import choice


def get_popular_word(message: str) -> str:
    words = message.lower().split()
    word_quantity_dict = {}
    for word in words:
        word_quantity_dict[word] = word_quantity_dict.get(word, 0) + 1
    max_number = max(word_quantity_dict.values())
    res = []
    for key, value in word_quantity_dict.items():
        if value == max_number:
            res.append(key)
    return choice(res)


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
        popular_word = get_popular_word(message.decode())
        client.sendall(popular_word.encode())
        if not data:
            break

server.close()

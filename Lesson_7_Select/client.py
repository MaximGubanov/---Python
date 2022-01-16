from socket import socket, AF_INET, SOCK_STREAM


def client():

    SOCK = socket(AF_INET, SOCK_STREAM)
    SOCK.connect(('localhost', 7777))

    while True:
        msg = input('Ввведите текст:\t')
        if msg == 'exit':
            break
        SOCK.send(msg.encode('utf-8'))
        data = SOCK.recv(1024).decode('utf-8')
        print(f'{data}\n')
    SOCK.close()


if __name__ == '__main__':
    client()
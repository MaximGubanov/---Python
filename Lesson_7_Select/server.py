import select
import logging
import server_log_config
from socket import socket, AF_INET, SOCK_STREAM

LOGGER = logging.getLogger('server')


def read_requests(r_clients, all_clients):
   responses = {}

   for sock in r_clients:
       try:
           data = sock.recv(1024).decode('utf-8')
           responses[sock] = data
       except Exception as e:
           LOGGER.info(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
           all_clients.remove(sock)
   return responses


def write_responses(requests, w_clients, all_clients):
   for sock in w_clients:
       if sock in requests:
           try:
               resp = requests[sock].encode('utf-8')
               for client in w_clients:
                    client.send(resp)
           except Exception as e:
               LOGGER.info(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
               sock.close()
               all_clients.remove(sock)


def create_socket(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(1)
    return s


def mainloop():
   ADDRESS = ('127.0.0.1', 7777)
   CLIENTS = []
   SOCK = create_socket(ADDRESS)

   while True:
       try:
           conn, addr = SOCK.accept()
       except OSError as e:
           pass
       else:
           LOGGER.info(f'Получен запрос на соединение от {str(addr)}')
           CLIENTS.append(conn)
       finally:
           wait = 10
           r, w = [], []
           try:
               r, w, e = select.select(CLIENTS, CLIENTS, [], wait)
           except Exception as e:
               pass

           requests = read_requests(r, CLIENTS)
           if requests:
               write_responses(requests, w, CLIENTS)


LOGGER.info('Cервер запущен!')


mainloop()
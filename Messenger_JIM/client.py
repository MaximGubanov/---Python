import os
import sys
from socket import AF_INET, SOCK_STREAM, socket
from utils import send_message, get_message
import time
import logging
import log.client_log_config
from log_decor import log

logger = logging.getLogger('client')


@log
def create_presence_message(account_name):
    if account_name:
        message = {
            os.getenv('ACTION'): os.getenv('PRESENCE'),
            os.getenv('TIME'): time.time(),
            os.getenv('USER'): {
                os.getenv('ACCOUNT_NAME'): account_name
            }
        }
        logger.info(f'Собщение создано успешно {message}')
        return message
    else:
        logger.error(f'Ошибка в account_name -> "{account_name}" - этот параметр не должен быть пустым')


@log
def parse_response(message):
    if os.getenv('RESPONSE') in message:
        if message[os.getenv('RESPONSE')] == 200:
            return '200 : OK'
        return f'400 : {message[os.getenv("ERROR")]}'
    logger.warning(f'Ошибка parse_response() -> {message}')
    raise ValueError


def main():
    global server_address, server_port

    try:
        if sys.argv[1] and sys.argv[2]:
            server_address, server_port = sys.argv[1], sys.argv[2]
            logger.info(f'Сервер запущен с параметрами: {server_address} {server_port}')
    except IndexError:
        server_address, server_port = os.getenv('DEFAULT_IP_ADDRESS'), os.getenv('DEFAULT_PORT')
        logger.info(f'Сервер запущен с параметрами по умолчанию {server_address} {server_port}')

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, int(server_port)))
    presence_message = create_presence_message('Guest')
    send_message(transport, presence_message)
    response = get_message(transport)

    logger.info(f'Ответ сервера: {response}')
    logger.info(f'{parse_response(response)}')


if __name__ == '__main__':
    main()
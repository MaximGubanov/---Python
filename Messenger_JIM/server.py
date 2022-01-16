import os
from socket import AF_INET, SOCK_STREAM, socket
import sys
from utils import send_message, get_message, load_cfg
import logging
import log.server_log_config
from log_decor import log

logger = logging.getLogger('server')


@log
def parse_message(message):
    if os.getenv('ACTION') in message \
            and message[os.getenv('ACTION')] == os.getenv('PRESENCE') \
            and os.getenv('TIME') in message \
            and os.getenv('USER') in message \
            and message[os.getenv('USER')][os.getenv('ACCOUNT_NAME')] == 'Guest':
        return {os.getenv('RESPONSE'): 200}
    else:
        logger.warning(f'В parse_message(), что-то пошло не так: {message}')
        return {
            os.getenv('RESPONSE'): 400,
            os.getenv('ERROR'): 'Bad Request'
        }


def main():
    load_cfg()
    global server_address, server_port
    try:
        if sys.argv[1] == '-a' and sys.argv[3] == '-p':
            head, a, server_address, p, server_port, *tail = sys.argv
            logger.info(f'Сервер запущен с адресом {server_address} на {server_port} порту')
            logger.debug('Режим отладки')
        else:
            raise NameError
    except IndexError:
        logger.warning('Команда введена без парамметров')
        server_address = ''
        server_port = os.getenv('DEFAULT_PORT')
        logger.info(f'Сервер запущен с настройками по умолчанию на {server_port} порту.')
    except NameError:
        logger.error('Пользователь ввёл некорректные параметры')
        logger.warning(f'Некорректно введены параметры. Попробуйте: $ python3 server.py -a [ip-адрес] -p [порт сервера]')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    logger.info(f'Сокет создан')
    transport.bind((server_address, int(server_port)))
    logger.info(f'Привязка адреса "{server_address}" к порту {server_port}')
    transport.listen(int(os.getenv('MAX_CONNECTIONS')))
    logger.info('Ожидание клиентов...')

    while True:
        client, address = transport.accept()
        logger.info(f'Успешно принял соединение от: {client}')
        message = get_message(client)
        response = parse_message(message)
        send_message(client, response)
        logger.info(f'Сообщение успешно отправлено')
        client.close()

        print(f'Запрос от клиента: {message}\n'
              f'Код ответа для клиента: {response}')


if __name__ == '__main__':
    main()
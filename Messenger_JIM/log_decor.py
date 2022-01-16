import logging
import sys
import inspect
from log import client_log_config, server_log_config

if sys.argv[0].split('.')[0] == 'server':
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')


def log(func):
    def log_decor(*args, **kwargs):
        f = func(*args, **kwargs)
        logger.debug(f'Функция: {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return f
    return log_decor


@log
def myfunc():
    print('my_func')


def my_main():
    myfunc()


my_main()
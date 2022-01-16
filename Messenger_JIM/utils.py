import os
import json
from dotenv import load_dotenv


def load_cfg():

    env = os.path.join(os.path.dirname(__file__), '.env')

    if os.path.exists(env):
        load_dotenv(env)
    else:
        print(f'Файл \'{env.split(".")[1]}\' не существует')


load_cfg()


def send_message(open_socket, message):
    json_message = json.dumps(message)
    response = json_message.encode(os.getenv('ENCODING'))
    open_socket.send(response)


def get_message(open_socket):
    response = open_socket.recv(int(os.getenv('MAX_PACKAGE_LENGTH')))
    if isinstance(response, bytes):
        json_response = response.decode(os.getenv('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError
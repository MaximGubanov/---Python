import os
from utils import get_message, send_message, load_cfg
import unittest
import json


class TestSocket:
    load_cfg()

    def __init__(self, test_message):
        self.test_message = test_message
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_message)
        self.encoded_message = json_test_message.encode(os.getenv('ENCODING'))
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_message)
        return json_test_message.encode(os.getenv('ENCODING'))


class Tests(unittest.TestCase):
    load_cfg()

    test_message_send = {
        os.getenv('ACTION'): os.getenv('PRESENCE'),
        os.getenv('TIME'): 111111.111111,
        os.getenv('USER'): {
            os.getenv('ACCOUNT_NAME'): 'test_test'
        }
    }
    test_success_receive = {os.getenv('RESPONSE'): 200}
    test_error_receive = {
        os.getenv('RESPONSE'): 400,
        os.getenv('ERROR'): 'Bad Request'
    }

    def test_send_message(self):
        test_socket = TestSocket(self.test_message_send)
        send_message(test_socket, self.test_message_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):
        test_sock_ok = TestSocket(self.test_success_receive)
        test_sock_err = TestSocket(self.test_error_receive)
        self.assertEqual(get_message(test_sock_ok), self.test_success_receive)
        self.assertEqual(get_message(test_sock_err), self.test_error_receive)


if __name__ == '__main__':
    unittest.main()
import unittest
from server import parse_message
from utils import load_cfg
import os


class TestServer(unittest.TestCase):

    load_cfg()

    success_messages = {os.getenv('RESPONSE'): 200}

    error_message = {
        os.getenv('RESPONSE'): 400,
        os.getenv('ERROR'): 'Bad Request'
    }

    def test_parse_message_type(self):
        self.assertEqual(type(parse_message({'status': 200})), dict)

    def test_parse_message_empty_dict_error(self):
        self.assertEqual(parse_message({}), self.error_message)

    def test_parse_message_without_action(self):
        self.assertEqual(parse_message({
                os.getenv('TIME'): '1.1',
                os.getenv('USER'): {
                    os.getenv('ACCOUNT_NAME'): 'Guest'
                }
            }), self.error_message)

    def test_parse_message_without_time(self):
        self.assertEqual(parse_message({
                os.getenv('ACTION'): os.getenv('PRESENCE'),
                os.getenv('USER'): {
                    os.getenv('ACCOUNT_NAME'): 'Guest'
                }
            }), self.error_message)

    def test_parse_message_without_user(self):
        self.assertEqual(parse_message({
                os.getenv('ACTION'): os.getenv('PRESENCE'),
                os.getenv('TIME'): '1.1',
            }), self.error_message)

    def test_parse_message_check_account_name(self):
        self.assertEqual(parse_message({
                os.getenv('ACTION'): os.getenv('PRESENCE'),
                os.getenv('TIME'): '1.1',
                os.getenv('USER'): {
                    os.getenv('ACCOUNT_NAME'): 'user'
                }
            }), self.error_message)

    def test_parse_message_check_success(self):
        self.assertEqual(parse_message({
                os.getenv('ACTION'): os.getenv('PRESENCE'),
                os.getenv('TIME'): '1.1',
                os.getenv('USER'): {
                    os.getenv('ACCOUNT_NAME'): 'Guest'
                }
            }), self.success_messages)


if __name__ == '__main__':
    unittest.main()

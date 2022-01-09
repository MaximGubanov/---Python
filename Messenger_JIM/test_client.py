import unittest
from utils import load_cfg
import os
from client import create_presence_message, parse_response


class TestClient(unittest.TestCase):

    load_cfg()

    def test_create_presence_message(self):
        test = create_presence_message('Guest')
        test[os.getenv('TIME')] = 1.1
        self.assertEqual(test, {
                os.getenv('ACTION'): os.getenv('PRESENCE'),
                os.getenv('TIME'): 1.1,
                os.getenv('USER'): {
                    os.getenv('ACCOUNT_NAME'): 'Guest'
                }
            }
        )

    def test_parse_response_success_request(self):
        self.assertEqual(parse_response({'response': 200}), '200 : OK')

    def test_parse_response_bad_request(self):
        self.assertEqual(parse_response({'response': 400, 'error': 'Bad Request'}), '400 : Bad Request')

    def test_parse_response_raise_error(self):
        self.assertRaises(ValueError, parse_response, {'error': 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
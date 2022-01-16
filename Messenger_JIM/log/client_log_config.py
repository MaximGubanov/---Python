import logging
import sys
import os

DIR_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.basename('client.log')
PATH = os.path.join(DIR_PATH, FILE_PATH)

logger = logging.getLogger('client')

format = logging.Formatter('%(asctime)s %(levelname)-10s %(name)s %(message)s')

info_hand = logging.StreamHandler(sys.stderr)
# info_hand.setLevel(logging.INFO)
info_hand.setFormatter(format)

err_hand = logging.FileHandler(PATH, encoding='utf-8')
err_hand.setFormatter(format)
err_hand.setLevel(logging.DEBUG)
logger.addHandler(err_hand)

logger.addHandler(info_hand)
logger.setLevel(logging.DEBUG)
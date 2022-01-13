import logging
from logging.handlers import TimedRotatingFileHandler
import sys
import os

DIR_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.basename('server.log')
PATH = os.path.join(DIR_PATH, FILE_PATH)

logger = logging.getLogger('server')

format = logging.Formatter('%(asctime)s %(levelname)-10s %(name)s %(message)s')

info_hand = logging.StreamHandler(sys.stderr)
info_hand.setLevel(logging.INFO)
info_hand.setFormatter(format)

time_hand = TimedRotatingFileHandler(PATH, when="D", interval=1, backupCount=5, utc=False)
time_hand.setFormatter(format)
time_hand.setLevel(logging.ERROR)
logger.addHandler(time_hand)
time_hand.doRollover()

logger.addHandler(info_hand)
logger.setLevel(logging.DEBUG)
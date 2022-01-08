import os
from dotenv import load_dotenv


env = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env):
    load_dotenv(env)
    print(os.getenv('KEY'))
else:
    print(f'Файл \'{env.split(".")[1]}\' не существует')


import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Парсинг переменных окружения
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")
WEB_SERVER_HOST = os.getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT = int(os.getenv("WEB_SERVER_PORT"))
MAIN_BOT_PATH = os.getenv("MAIN_BOT_PATH")
OTHER_BOTS_PATH = os.getenv("OTHER_BOTS_PATH")
OTHER_BOTS_URL = f"{BASE_URL}{OTHER_BOTS_PATH}"

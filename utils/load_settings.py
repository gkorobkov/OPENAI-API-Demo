
import os
import json

from dotenv import find_dotenv, load_dotenv


# Загрузка файла настроек
def load_settings(settings_path: str) -> dict:
    """load_settings."""
    with open(settings_path, 'r', encoding='utf-8', errors='replace') as file:
        return json.load(file)


load_dotenv()  # Load variables from .env file
root_path = os.getcwd()
settings_path = os.path.abspath(os.path.join(root_path, os.getenv('SETTINGS_PATH')))
# print ("Loading settings from: " + settings_path)

settings = load_settings(settings_path)
# print(settings)

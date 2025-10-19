import os
import json

from dotenv import find_dotenv, load_dotenv

from utils.load_settings import settings

# Загрузка базы данных курсов
def load_database(file_path: str) -> list[dict]:
    """load_database"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

load_dotenv()  # Load variables from .env file
root_path = os.getcwd()

course_data_path = os.path.abspath(os.path.join(root_path, settings["course_data_path"]))
# print("Loading data from: " + course_data_path)

courses_database = load_database(course_data_path)
# print(courses_database)

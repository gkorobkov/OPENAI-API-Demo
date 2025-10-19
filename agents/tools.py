
import os
from rapidfuzz import fuzz, process
from datetime import datetime
from langchain.tools import tool
from utils.load_data import courses_database
from utils.load_settings import settings



@tool
def get_all_course_names() -> str:
    """
    Return, for example, names of 3-5 courses from {courses_database}. 
    If the user mentions their role (role), suggest courses based on difficulty level or provide a detailed description of one course that best matches the user's request.
    """
    return ", ".join([course["name"] for course in courses_database])


@tool
def get_most_similar_course(name: str) -> dict:
    """
    Return course information by exact title from the database.

    Args:
    name (str): Exact course title.

    Returns:
    Dict: Dictionary containing course information (role, skills, difficulty, description, link).
    """
    name = name.strip().lower()
    if not courses_database:
        return {"error": "DB courses_database is empty."}

    course_names = [course["name"].lower() for course in courses_database]
    match = process.extractOne(name, course_names, scorer=fuzz.partial_ratio)

    if match and match[1] >= settings["default_similarity_threshold"] * 100:  
        matching_course_index = course_names.index(match[0])
        return courses_database[matching_course_index]
    else:
        return {"error": "NO course for specific name."}


@tool
def register_for_course(course_name: str, course_link: str, user_name: str, user_surname: str) -> str:
    """
    Requests user's first and last names, then returns a message confirming enrollment in the course.

    Arguments:

    - course_name (str): Name of the course the user is enrolling in.
    - course_link (str): Link to the course.
    - user_name (str): User's first name.
    - user_surname (str): User's last name.

    Returns:

    - str: Confirmation message for course enrollment including keys {first name}, {last name}, {course name}, {date}, {course link}.
    """
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    confirmation_message = (
        f"Hello, {user_name} {user_surname}!\n"
        f"You have successfully enrolled in the course '{course_name}'.\n"
        f"Enrollment date: {current_date}\n"
        f"Course link: {course_link}"
    )
    
    return confirmation_message




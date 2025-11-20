def generate_profile(age: int) -> str:
    # Determine user's life stage based on their age.
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"


# Get user input
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

# Calculate current age
from datetime import datetime

current_year = datetime.now().year
current_age = current_year - birth_year

# Initialize hobbies list and Loop to collect hobbies
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

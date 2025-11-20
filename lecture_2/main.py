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
user_name: str = input("Enter your full name: ")
birth_year_str: str = input("Enter your birth year: ")
birth_year: int = int(birth_year_str)

# Calculate current age
from datetime import datetime

current_year: int = datetime.now().year
current_age: int = current_year - birth_year

# Initialize hobbies list and Loop to collect hobbies
hobbies: list[str] = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

# Process and Generate the Profile

# Call generate_profile to get the life stage
life_stage:str = generate_profile(current_age)

# Create user-profile dict
user_profile = {
    "name": user_name,
    "age": current_age,
    'stage': life_stage,
    "hobbies": hobbies,
}
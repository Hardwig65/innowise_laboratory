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

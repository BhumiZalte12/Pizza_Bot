import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

def extract_session_id(session_str: str):
    # Corrected to return group(1) which contains only the session ID
    match = re.search(r'/sessions/([^/]+)/contexts/', session_str)
    if match:
        extracted_string = match.group(1)  # This extracts only the session ID
        return extracted_string

    return ""

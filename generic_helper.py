# Author: Dhaval Patel. Codebasics YouTube Channel

import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    

    return ""


   
    #extract_session_id("projects/chatbot-iptb/agent/sessions/ad08a5ce-3f44-3b71-e538-a1f077bcb8ef/contexts/ongoing-order")
    #get_str_from_food_dict({"pizza":2,"samosa":3})

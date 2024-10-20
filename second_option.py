"""
Here I want to show the option to solve the task through simple functions in Python. 
I my opinion, this is the shortest possible solution
"""

import json

def read_animal_sound(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    
    
    if data.get("field1") != "value1":
        return "Invalid data: field1 must be 'value1'"
    
    if set(data.keys()) != {"field1", "animal"}:
        return "Invalid data: Only 'field1' and 'animal' fields are allowed"      
    
    sounds = {
        "dog": "bark",
        "cat": "meow",
        "cow": "moo",
        "rat": "pipi",
        "alien": "KILL"
    }

    animal = data.get("animal", "")

    return sounds.get(animal, "Unknown sound")


if __name__ == "__main__":
    print(read_animal_sound(file_path="right directory"))

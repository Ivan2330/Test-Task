"""
Here I want to show the option to solve the task through an abstract class in Python. 
I chose that option, because I think that it's the most comfortable way to add and change something in case of need
"""

import json
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod 
    def get_sound(self):
        pass
    
class Dog(Animal):
    def get_sound(self):
        return "bark"
    
class Cat(Animal):
    def get_sound(self):
        return "meow"
    
class Cow(Animal):
    def get_sound(self):
        return "moo"
    
class Rat(Animal):
    def get_sound(self):
        return "pipi"
    
class Alien(Animal):
    def get_sound(self):
        return "KILL"
    
class AnimalGroup:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            "dog": Dog(),
            "cat": Cat(),
            "cow": Cow(),
            "rat": Rat(),
            "alien": Alien(),
        }
        return animals.get(animal_type, None)
    
def main():
    try:
        with open("test.json", "r") as file:
            data = json.load(file)
            
            if data.get("field1") != "value1":
                print("Invalid input: field1 must be 'value1")
                
        animal_type = data.get("animal")
        animal = AnimalGroup.create_animal(animal_type)
        
        if animal:
            print(animal.get_sound())
        else:
            print("Unknown animal")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file {e}")
        
if __name__=="__main__":
    main()
            
            

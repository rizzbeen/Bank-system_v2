import pwinput
import colorama
import json
from datetime import datetime
import random

# Color functions for terminal output
def black(text):
    return colorama.Fore.BLACK + text + colorama.Style.RESET_ALL

def red(text):
    return colorama.Fore.RED + str(text) + colorama.Style.RESET_ALL

def green(text):
    return colorama.Fore.GREEN + str(text) + colorama.Style.RESET_ALL

def yellow(text):
    return colorama.Fore.YELLOW + str(text) + colorama.Style.RESET_ALL

def blue(text):
    return colorama.Fore.BLUE + str(text) + colorama.Style.RESET_ALL

def magenta(text):
    return colorama.Fore.MAGENTA + str(text) + colorama.Style.RESET_ALL

def cyan(text):
    return colorama.Fore.CYAN + str(text) + colorama.Style.RESET_ALL

def white(text):
    return colorama.Fore.WHITE + str(text) + colorama.Style.RESET_ALL

# Secure PIN input for account creation
def create_pin():
    enter = green("\nCREATE A 4 DIGIT PIN:\t")
    data = pwinput.pwinput(prompt=enter, mask="*").strip()
   
    if len(data) != 4 or not data.isdigit():
        print(red("❌ PLEASE ENTER A VALID PIN"))
        raise ValueError("PLEASE ENTER A VALID PIN")
    if not data.strip():
        print(red("❌ PIN CANNOT BE EMPTY"))
        raise ValueError("PIN CANNOT BE EMPTY")

    return data

# Ask for PIN input (with masking)
def ask_pin(text):
    enter = green(text + ":\t")
    return pwinput.pwinput(prompt=enter, mask="*").strip()

# Save Python dictionary to JSON file
def save_json(data):  
    try:
        with open("data/users.json", "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print(red("❌ FILE NOT FOUND"))

# Read JSON file and return as dictionary
def read_json():  
    try:
        with open("data/users.json", "r") as file:
            user_data = file.read().strip()
            if not user_data:
                return {}
            return json.loads(user_data)
    except FileNotFoundError:
        print(red("❌ FILE NOT FOUND"))      

# Generate a unique 4-digit user ID
def generate_userid(user_data):  
    while True:
        try:
            uniqueID = str(random.randint(1000, 9999))
            if uniqueID not in user_data:
                return uniqueID
        except Exception:
            print(red("❌ SOMETHING WENT WRONG PLEASE TRY AGAIN LATER"))  

# Return current date and time as string
def date_time(): 
    return datetime.now().strftime("%d-%m-%y %H-%M-%S")


     
      

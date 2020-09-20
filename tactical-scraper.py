#Coded by:fbitactical on Instagram.
#A-Python2-Phonenumber-Information-Scraper

from phonenumbers import *
import requests

print()
print("▄▄▄█████▓ ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▄████▄   ▄▄▄       ██▓ ")   
print("▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒ ")   
print("▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░ ")   
print("░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░   ") 
print("  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒ ")
print("  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░ ")
print("    ░      ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ")
print("  ░        ░   ▒   ░          ░       ▒ ░░          ░   ▒     ░ ░    ")
print("               ░  ░░ ░                ░  ░ ░            ░  ░    ░  ░ ")
print("                   ░                     ░                           ")
print()

phone_number = input("Enter a phone-number: ")
response = requests.get("http://apilayer.net/api/validate?access_key=0934c36cd49141e24778e5dffa755e5b&number=" + phone_number + "&country_code=US")

print(response.json())

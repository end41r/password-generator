import random

SPECIFIED = True
NUMBERS = True


password_file = open("passwords.txt", "w")

# Questions

website = input("Write in a website, where you want to register: ")
name = input("Write a name if you want to create multiple accounts on a single website: ")
specified_choice = input("Do you want specified symbols like !^&*%# to be in the password?: (Y/n) ")

if specified_choice == "Y":
	SPECIFIED = True
else:
	SPECIFIED = False

numbers_choice = input("Do you want numbers to be in password?: (Y/n) ")

if numbers_choice == "Y":
	NUMBERS = True
else:
	NUMBERS = False

# Lists with symbols

list_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_specified = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', '"', "'", '/', '?', ',', '.', '<', '>', '\\', '|', '~', '`', '[', ']', '{', '}']

# Password generation

random.shuffle(list_small)
random.shuffle(list_big)
random.shuffle(list_numbers)
random.shuffle(list_specified)

if NUMBERS == True and SPECIFIED == True:
	list_full = list_small + list_big + list_numbers + list_specified
elif NUMBERS != True and SPECIFIED == True:
	list_full = list_small + list_big + list_specified
elif NUMBERS == True and SPECIFIED != True:
	list_full = list_small + list_big + list_numbers
elif NUMBERS != True and SPECIFIED != True:
	list_full = list_small + list_big

random.shuffle(list_full)
symbols_choice = input("How many symbols do you want to have in your password (We recommend to use passwords from 16 symbols or even more!): ")
password = ''
for i in range(int(symbols_choice)):
	password += random.choice(list_full)

print("This is your password: " + password + "\n it will be saved in a file passwords.txt")


password_file.write(str(website) + ", " + str(name) + ": " + password + "\n")

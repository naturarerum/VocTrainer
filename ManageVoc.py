import json
import os
import random
import sys

word_dict = {}
file_name = 'c:\\tmp\\data\\word_dict.json'


def add_word_from_input():
    while True:
        key = input("Enter key - type exit to end : ")
        # break loop if user enters "exit"
        if key == "exit":
            break
        value = input("Enter value: ")
        if key in word_dict:
            print("key already exists")
            continue
        word_dict[key] = value
        print(word_dict)
        save_dict_to_file(word_dict)
    return word_dict


def save_dict_to_file(dico):
    # Serialize data into file
    try:
        with open(file_name, 'w') as f:
            json.dump(dico, f)
    except ValueError as e:
        print(f"Error: Unable to decode JSON, Error: {e}")


def pick_random_word(word_dict):
    position = random.randint(0, len(word_dict) - 1)
    print(position)
    key = list(word_dict.keys())[position]
    return key, word_dict[key]


def read_dict_from_file():
    # read data from file:
    try:
        with open(file_name, 'r') as f:
            dico = json.load(f)
            print(dico)
    except FileNotFoundError as e:
        print(f"Error: Unable to find file, Error: {e}")
    return dico


def guess_the_word(word_dict):
    for key, value in word_dict.items():
        print(f"Key: {key}, Value: {value}")
    guess = input("Enter your guess: ")
    if guess in word_dict.values():
        print("Congratulations! You guessed the word.")
    else:
        print("Sorry, that's not the word.")


def done():
    os.system('clear')  # clears stdout
    print("Goodbye")
    sys.exit()


def main_menu():
    print("************ Menu *******************")
    print("1.Input new word")
    print("2.Display the dictionary")
    print("3.Knowledge test")
    print("4.Exit")
    print("*************************************")
    choice: str = input("Select an option : ")

    if choice == "1":
        add_word_from_input()
        save_dict_to_file()
    if choice == "2":
        read_dict_from_file()
    #if choice == "3":
    #    read_dict_from_file()
    if choice == "4":
        done()


# word_dict = read_dict_from_file(dict)
# element = pick_random_word(word_dict)
# print(f"L'élément à la position est : {element}")
# add_word_from_input()

# guess_the_word(element)
if __name__ == "__main__":
    read_dict_from_file()
    main_menu()

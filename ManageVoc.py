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


def read_dict_from_file():
    # read data from file:
    try:
        with open(file_name, 'r') as f:
            dico = json.load(f)
            print(dico)
    except FileNotFoundError as e:
        print(f"Error: Unable to find file, Error: {e}")
    return dico


def guess_the_word():
    good_answer = 0
    number_of_runs = 0
    while True:
        key, value = random.choice(list(word_dict.items()))
        # print(f"Clé: {key}, Valeur: {value}")
        print("traduire :", key)
        number_of_runs += 1
        guess = input("Enter your guess (type exit to end process): ")
        if guess == "exit":
            break
        if guess == value:
            print("Congratulations! You guessed the word.")
            good_answer += 1
        else:
            print("Sorry, that's not the word.")
    return good_answer, number_of_runs


def calculate_score():
    pass


def done():
    os.system('clear')  # clears stdout
    print("Goodbye")
    sys.exit()


word_dict = read_dict_from_file()
add_word_from_input()
good_a, nb_runs = guess_the_word()
print(good_a, nb_runs)

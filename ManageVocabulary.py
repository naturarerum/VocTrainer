import FileManager

class ManageVocabulary:

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
import json


class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_dict_from_file(self):
    # read data from file:
        try:
            with open(self.file_name, 'r') as f:
                self.dico = json.load(f)
                #print(self.dico)
        except FileNotFoundError as e:
            print(f"Error: Unable to find file, Error: {e}")
        return self.dico
    
    def save_dict_to_file(self):
        # Serialize data into file
        try:
            with open(self.file_name, 'w') as f:
                json.dump(self.dico, f)
        except ValueError as e:
            print(f"Error: Unable to decode JSON, Error: {e}")


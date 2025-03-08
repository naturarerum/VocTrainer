from FileManager import FileManager
from WordTraining import WordTraining

class ManageVocabulary:
    def __init__(self,dic):
        self.dic = dic

    def add_word_from_input(self):
        while True:
            key = input("Enter key - type exit to end : ")
            # break loop if user enters "exit"
            if key == "exit":
                break
            value = input("Enter value: ")
            if key in self.dic:
                print("key already exists")
                continue
            self.dic[key] = value
            print(self.dic)
            #save_dict_to_file(word_dict)
        #return word_dict
        
     
    def print_dictionnary_content(self):
        print(f"Contenu du dictionnaire : {self.dic}")
    

def main():
    print('*** running object oriented version ****')
    
    filemanager = FileManager('/mnt/chromeos/MyFiles/Linuxfiles/VocTrainer/word_dict.json')
    word_dict = filemanager.read_dict_from_file()
    managevoc = ManageVocabulary(word_dict)
    managevoc.add_word_from_input()
    managevoc.print_dictionnary_content()
    filemanager.save_dict_to_file()
    training = WordTraining(word_dict)
    training.guess_the_word()
   
    
#    

if __name__ == "__main__":
    main()

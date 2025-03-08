import random
#from FileManager import FileManager


class WordTraining:
    def __init__(self,dic):
        self.dic = dic
        self.good_answer = 0
        self.bad_answer = 0
        self.number_of_runs = 0

    
    def guess_the_word(self):
        
        while True:
            key, value = random.choice(list(self.dic.items()))
            # print(f"Clé: {key}, Valeur: {value}")
            print("traduire :", key)
            #number_of_runs += 1
            self.guess = input("Enter your guess (type exit to end process): ")
            if self.guess == "exit":
                break
            if self.guess == value:
                print("Congratulations! You guessed the word.")
                self.good_answer += 1
            else:
                print("Sorry, that's not the word.")
                self.bad_answer += 1
        

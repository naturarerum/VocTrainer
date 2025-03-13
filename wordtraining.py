import random


class WordTraining:
    def __init__(self, dic):
        self.dic = dic
        self.good_answer = 0
        self.bad_answer = 0
        self.number_of_runs = 0

    def guess_the_word(self):
        
        while True:
            key, value = random.choice(list(self.dic.items()))
            print("traduire :", key)
            self.guess = input("Enter your guess (type exit to end process): ")
            if self.guess == "exit":
                break
            if self.guess == value:
                self.number_of_runs += 1
                print("Congratulations! You guessed the word.")
                self.good_answer += 1
            else:
                print("Sorry, that's not the word.")
                self.bad_answer += 1
                
    def display_score(self):
        print(f"Total number of runs : {self.number_of_runs}")
        print(f"Total number of good answers : {self.good_answer}")
        

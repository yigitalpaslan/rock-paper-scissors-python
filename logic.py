import random as rd


class RandomChoice():
    
    def __init__(self):
        self.random_list = ["Rock","Scissor","Paper"]
        self.comp_counter = 0
        self.user_counter = 0
        self.draw_counter = 0

    def get_computer_choice(self):
        self.random_choice = rd.choice(self.random_list)
        return self.random_choice
    
    def compare(self,users_choice, computer_choice):
        if users_choice == computer_choice:
            self.draw_counter += 1
            return "Draw"
        
        elif (users_choice=="Rock" and computer_choice=="Scissor" or \
            users_choice=="Paper" and computer_choice=="Rock" or \
            users_choice=="Scissor" and computer_choice=="Paper"):
            self.user_counter+=1
            return "You Won :)"
        
        else:
            self.comp_counter+=1
            return "You Lose :("
        
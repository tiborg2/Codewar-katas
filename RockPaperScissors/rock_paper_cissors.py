'''
Function to play rock, paper, scissors game against AI'''
import random as rn

def rock_paper_scissors():
    class AI:
        def __init__(self, name):
            self.name = name
            self.score = 0
            self.pick = ''
        
        def picker(self):
            self.pick = rn.choice(["rock", "paper", "scissors"])
            
    computer = AI("Super Kompas")
    computer.picker()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.pick = ''
    
    def error_handler(self, choice):
        choices = ["rock", "paper", "scissors"]
        if choice in choices:
            return True
        else:
            return False
    

    def picker(self):
        n = input('Please insert "r" for "Rock"')
        pass




print(error_handler("pl", "rocky"))
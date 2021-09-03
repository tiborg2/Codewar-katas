'''
Function to play rock, paper, scissors game against AI
'''
import random as rn

def rock_paper_scissors():
    choices1 = ["Rock", "Paper", "Scissors"]
    choices = ['r', 'R', 'p', 'P', 's', 'S']
    choice_hash = {'r':"Rock", 'p':"Paper", 's':"Scissors", 'R':"Rock", 'P':"Paper", 'S':"Scissors"}

    def call_selector(): #Calls choice table.Utility.
        with open ('selection_text.txt', 'r') as text:
            sl = text.read()
        print(sl)
        return sl
    
    def ai_picker():#Randomizes AI pick
        ai_pick = rn.choice(choices)
        return ai_pick        

    def error_handler(pl_pick): #Handles input errors.
        if pl_pick in choices:
            return True
        else:
            return False

    def pl_picker():#Player pick. 
        pl_pick = input('Your Choice: ')
        return pl_pick
    
    '''================Action start========================='''

    ai_pick = choice_hash.get(ai_picker())
    print (ai_pick)
    sl = call_selector()
    pl_pick = pl_picker()

    #pl_pick = choice_hash.get(pl_picker())
    #print (f'"You choosed: {pl_pick}')
    
    if pl_pick != 'q' or pl_pick != 'Q':
        if error_handler(pl_pick):
            print(f'Going to compare Player {pl_pick} and Computer {ai_pick}')
        else:
            print (f'Error message')
    else:
        return 'O'





rock_paper_scissors()
#print(error_handler("pl", "rocky"))
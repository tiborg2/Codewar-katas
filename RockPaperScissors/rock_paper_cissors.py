import random as rn
import os
import time
'''
Function to play rock, paper, scissors game against AI
'''
def rock_paper_scissors():
    '''================Primary Data=========================='''

    choices1 = ["Rock", "Paper", "Scissors"]
    choices = ['r', 'p', 's', 'q']
    choice_hash = {'r':"Rock", 'p':"Paper", 's':"Scissors"}
    pl_count = 0
    ai_count = 0
    line = f'**************************************************'

    '''================Function Part========================='''

    def call_selector(): #Calls choice table.Utility.
        with open ('selection_text.txt', 'r') as text:
            sl = text.read()
        print(sl)
        return sl
    
    def cls(): # Terminar clearance. Utility
        os.system('cls' if os.name=='nt' else 'clear')

    def ai_picker():#Randomizes AI pick
        ai_pick = rn.choice(choices)
        return ai_pick        

    def error_handler(pl_pick): #Handles input errors.
        if pl_pick in choices:
            return True
        else:
            return False

    def pl_picker():#Player's pick. 
        pl_pick = input('Your Choice: ')
        pl_pick = pl_pick.lower()
        return pl_pick
    
    '''================Action Part=========================='''

    ai_pick = choice_hash.get(ai_picker())
    sl = call_selector()
    pl_pick = pl_picker()
    #print(pl_pick)

    #pl_pick = choice_hash.get(pl_picker())
    #print (f'"You choosed: {pl_pick}')
    
    if pl_pick == 'q':
        print ("Bye!")
        return 0
    else:    
        if error_handler(pl_pick):
            plh_pick = choice_hash.get(pl_pick)
            cls()
            print(line)
            print(f'Going to compare Player: "{plh_pick}" and Computer: "{ai_pick}"')
            print(line)
            time.sleep(5)
        else:
            print (f'Error message')
    
    return 0

rock_paper_scissors()
#print(error_handler("pl", "rocky"))
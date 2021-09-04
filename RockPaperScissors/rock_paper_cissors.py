import random as rn
import os
import time
'''
Rock, paper, scissors game against AI.
'''

'''================Primary Data=========================='''

#choices1 = ["Rock", "Paper", "Scissors"]
choices = ['r', 'p', 's']
choice_hash = {'r':"Rock", 'p':"Paper", 's':"Scissors"}
pl_result = 0
ai_result = 0
line = f'**************************************************'

'''================Function Part========================='''

def call_selector(): #Calls player's choice table.Utility.
    with open ('selection_text.txt', 'r') as text:
        sl = text.read()
    print(sl)
    return sl

def result_table(): #Calls result table top. Utility.
    with open ('score_text.txt', 'r') as text:
        global ai_result
        global pl_result
        st = text.read()
        print(st, end='')
        print(f'                        |*     {pl_result}               {ai_result}        *|')
        print (f'                        |*                              *|')
        print (f'                        **********************************')

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

def compare(plh_pick, ai_pick):#Comparisson finction. !Modifies results!
    global ai_result
    global pl_result
    if plh_pick == "Rock" and ai_pick == "Scissors":
        pl_result += 1
        print (line)
        print(f'You Score!')
        print (line)
    elif plh_pick == "Paper" and ai_pick == "Rock":
        pl_result += 1
        print (line)
        print(f'You Score!')
        print (line)
    elif plh_pick == "Scissors" and ai_pick == "Paper":
        pl_result += 1
        print (line)
        print(f'You Score!')
        print (line)
    elif plh_pick == "Scissors" and ai_pick == "Rock":
        ai_result += 1
        print (line)
        print(f'You Missed!')
        print (line)
    elif plh_pick == "Rock" and ai_pick == "Paper":
        ai_result += 1
        print (line)
        print(f'You Missed!')
        print (line)
    elif plh_pick == "Paper" and ai_pick == "Scissors":
        ai_result += 1
        print (line)
        print(f'You Missed!')
        print (line)
    else:
        print (line)
        print(f'Draw')
        print (line)
    if pl_result > ai_result:
        return 1
    elif pl_result < ai_result:
        return -1
    else:
        return 0

'''================Action Part=========================='''

sl = call_selector()
while pl_result < 3 or ai_result < 3: #Play loop. For some reason DOES NOT BREAK CORRECTLY.
    ai_pick = choice_hash.get(ai_picker())
    pl_pick = pl_picker()

    if pl_pick == 'q':
        print ("Bye!")
        break
    else:    
        if error_handler(pl_pick):
            plh_pick = choice_hash.get(pl_pick)
            cls()
            print(line)
            print(f'Going to compare Player: "{plh_pick}" and Computer: "{ai_pick}"')
            print(line)
            time.sleep(3)
            cls()
            compare(plh_pick, ai_pick)
            result_table()
            time.sleep(5)
            cls()
            print(sl)
        else:
            cls()
            print(line)
            print (f"Oops! Seems you've typed wrong button!")
            print(line)
            time.sleep(3)
            cls()
            print(sl)    
    if pl_result == 3 or ai_result == 3: #Forced loop break!
        if pl_result > ai_result:
            cls()
            print("You won")
            break
        else:
            cls()
            print("You lost")
            break

'''=================Final Part=========================='''

print("Bye!")





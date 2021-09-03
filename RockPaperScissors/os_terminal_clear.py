import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

choice_hash = {'r':"Rock", 'p':"Paper", 's':"Scissors"}

line = f'**************************************************'
def compare(plh_pick, ai_pick):
    ai_result = 0
    pl_result = 0
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
    return pl_result, ai_result
pl_count = 0
ai_count = 0
def score_update(pl_res, ai_res):
    pl_count += pl_res


print(compare('Rock', 'Rock'))

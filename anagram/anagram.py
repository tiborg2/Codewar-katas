from itertools import permutations
from datetime import datetime
t1 = datetime.now()
def perm (str):    
    x = list(permutations(str, len(str)))
    word = ''
    temp =[]
    for i in x:
        print(i)
        word = ''.join(i)
        temp.append(word)
        temp.sort() 
    for ind in range(len(temp)):
        if temp[ind] == str:            
            return ind
    return -1    



print(perm('DACA'))
print (datetime.now() - t1)
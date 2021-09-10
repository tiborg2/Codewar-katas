import itertools as itt
def permutations (str):
    tpl = tuple(str)
    temp = list(itt.permutations(tpl, len(tpl)))
    word = ''
    res = []
    ''' for item in temp:
        word = word.join(item)
        res.append(word)'''
    
    print (tpl)
    print (temp)
    print (res)
    '''for i in len(tpl):
        if tpl[i] == str:
            return tpl[i]'''  

print(permutations('AABA'))

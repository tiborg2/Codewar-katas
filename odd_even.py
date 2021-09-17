'''Function counts pairs of odd and even digits. 
    If digits pair  are odd and even function returns True, 
    else returns False.'''

#My solution
def lovefunc( flower1, flower2 ):
    if flower1 == 0 and flower2 == 0:
        return False 
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    if flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False

print(lovefunc(8, 9))




#Excellent solution
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
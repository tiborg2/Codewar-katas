def recursion(x): #Sums of all digits starting 0 to x inclusive.        
    if x < 0:
        if x == -1:
            return x
        else:
            z = (x + (recursion(x + 1)))
            return z
    if x == 0 or x == 1:
        return x
    else: 
        z = (x + (recursion (x -1)))        
        return z

    
print(recursion(12 ))


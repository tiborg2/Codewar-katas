def make_str(digit, count):
    first = digit - count
    text = f"{first}-{digit}"
    return text

def while_next(args):
    for i in range(len(args)):
        if i < len(args)-1:
            count = 0
            while args[i]+1 == args[i+1]:
                count += 1
                if i < len(args) - 1:                
                    i += 1           
        print(args[i])
    



# print (make_str(-1, 2))
while_next([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,26])
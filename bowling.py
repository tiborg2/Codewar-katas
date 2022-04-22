# My solution
def bowling_pins(arr):
    bowling_position = {7:[0, 0], 8:[2, 0], 9:[4, 0], 10:[6, 0],# Bowling position
                        4:[1, 1], 5:[3, 1], 6:[5, 1], 
                        2:[2, 2], 3:[4, 2],
                        1:[3, 3]}
    for item in arr:
        bowling_position.pop(item) 
    bowls_list = list()
    def check_position (x, y):
        answer = []
        for item in bowls_list:    
            if item[0] == x and item[1] == y:
                answer.append(True)
            else:
                answer.append(False)
        if True in answer:
            return True
        else:
            return False

    for x in bowling_position.values():
        bowls_list.append(x)
    rez = '\b'
    for y in range (0, 4):
        for x in range (0, 7):
            if check_position(x, y):    
                rez += 'I'                                        
            else:
                rez += ' '
            if x == 6 and y != 3:
                rez += '\n'
    rez = rez.lstrip("\b")
    return rez

print (bowling_pins([1, 2, 4, 6, 7, 8, 10]))


#Nice solution
def bowling_pins(arr):
    pins = [7,8,9,10,4,5,6,2,3,1]
    pins_after= []
    for pin in pins:
        if pin in arr:
            pins_after.append(' ')
        else:
            pins_after.append('I')
            
    
    
    return '{} {} {} {}\n {} {} {} \n  {} {}  \n   {}   '.format(*pins_after)
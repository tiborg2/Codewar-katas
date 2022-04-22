def survivors(list_of_momentum, list_of_powerups):
    tmp = set()
    def power_limit (mov, pwup, index):
        power = mov[index] - 1
        for x in range (0, len(pwup[index])):
            power += pwup[index][x]
        if power >= len(pwup[index]):
            return True
        else:
            return False

    def distance (mov, pwup, index):
        power = mov[index] - 1
        if power >= len(pwup[index]):
            return True
        for x in range (0, len(pwup[index])):
            #print(x)
            way = set()
            if (power + pwup[index][x]) > 0:
                power += pwup[index][x]
                way.add(True)
            else:
                way.add(False)
        if False in way:
            return False
        else:
            return True        

    for index in range (0, len(list_of_momentum)):
        if list_of_momentum[index] > 0:
            if power_limit(list_of_momentum, list_of_powerups, index):
                if distance (list_of_momentum, list_of_powerups, index):
                    tmp.add(index)
    out = list(tmp)            
    return out


list_of_momentum = [1,1,5,7,2,5,6,2,6,3,2,6,8,6,9,2,8,7]
mov = list_of_momentum
list_of_powerups =  [[],
                    [3,0],
                    [0,0,0,0,8,0,0,0],
                    [0,3,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0],
                    [0],
                    [],
                    [0],
                    [0,0,0,0,0,7,0],
                    [0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0],
                    [0],
                    [5,0,0,0,0,7],
                    [0],
                    [0,0,1,0,0,1,0]]

print(survivors(list_of_momentum, list_of_powerups))
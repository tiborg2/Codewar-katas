

listOfMomentum = [3, 2, 1, 0]
mov = listOfMomentum
listOfPowerups = [[1, 0, 0], [0, 2, 0, 0], [0, 9], [8, 8]]
pwup = listOfPowerups

#print (listOfPowerups[0])
def power_limit (mov, pwup, index):
    power = mov[index]
    if power >= len(pwup[index]):
        return True
    for x in range (0, len(pwup[index])):
        power += pwup[index][x]
        print(power)

    if power >= len(pwup[index]):
        return True
    else:
        return False

def distance (mov, pwup, index):
    power = mov[index]
    if power >= len(pwup[index]):
        return True
    for x in range (0, len(pwup[index])):
        #print(x)
        way = set()
        if (power + pwup[index][x]) >= x + 1:
            power += pwup[index][x]
            way.add(True)
        else:
            way.add(False)
    if False in way:
        return False
    else:
        return True


print (distance (mov, pwup, 1))
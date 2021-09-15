bowling_position = {7:(0, 0), 8:(2, 0), 9:(4, 0), 10:(6, 0),# Bowling psition
                        4:(1, 1), 5:(3, 1), 6:(5, 1), 
                        2:(2, 2), 3:(4, 2),
                        1:(3, 3)}
x = 0
y = 0
if x in bowling_position.values() and y in bowling_position.values():
    print (bowling_position.values())

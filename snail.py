def snail(snail_map):
    out = list()
    if snail_map == [[]]:
        return out
    limit = len(snail_map)
    limit_l = 0
    y = 0
    x = 0
    while limit > 0:
        while x < limit:
            out.append(snail_map[y][x])
            if len(out) == len(snail_map) ** 2:
                return out               
            x += 1
        x -= 1
        y += 1
        while y < limit:
            out.append(snail_map[y][x])
            if len(out) == len(snail_map) ** 2:
                return out
            y += 1
        y -= 1
        x -= 1
        while x >= limit_l:
            out.append(snail_map[y][x])
            if len(out) == len(snail_map) ** 2:
                return out
            x -= 1
        x += 1
        limit_l += 1
        y -= 1
        while y >= limit_l:
            out.append(snail_map[y][x])
            if len(out) == len(snail_map) ** 2:
                return out
            y -= 1
        y += 1    
        x += 1
        limit -= 1
    return out
    




array = [[]]

""" array = [[1,2,3,0],
         [4,5,6,1],
         [7,8,9,8],
         [1,3,4,5]] """
print(len(array))
print (array)
print(snail(array))         
expected = [1,2,3,6,9,8,7,4,5]

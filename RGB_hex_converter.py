def convert (*rgb):    
    out = '#'
    for item in rgb:
        temp = hex(item)
        out += temp[2:]
    return out


print(convert(100, 200, 255))

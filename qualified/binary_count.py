''' Function takes list of 3 decimail digits, converts every digit to 8 digit long binary, 
    connect these three inaries to one 24 digit long string and return decimail value of 
    this string.'''
def binary_count(arr):
    tmp = ''    
    for n in arr:
        bn = bin(n)
        stn = bn[2:]
        if len(stn) < 8:
            stn = stn.rjust(8, '0')
            tmp += stn
        else:
            tmp += stn
    out = int(tmp, 2)     
    return out, tmp



# Test
a = [0, 101, 251]
print(binary_count(a))
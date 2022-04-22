def x(n):
    D = chr(9633)
    L = chr(9632)
    out = ''
    for y in range (0, n//2): # Top part        
        if y == 0:
            out += f'{L}{D*(n-2)}{L}'
            #print(out, '\n')  
        else:                         
            out += f'{D*y}{L}{D*(n - (2 + 2*y))}{L}{D*y}'
            #print(out, '\n')  
        out += '\n'
    out += f'{D*(n//2)}{L}{D*(n//2)}\n' # Middle
    for y in range ((n//2-1), -1, -1): # Buttom part
        #print (y)        
        if y == 0:
            out += f'{L}{D*(n-2)}{L}'
            #print(out, '\n')  
        else:                         
            out += f'{D*y}{L}{D*(n - (2 + 2*y))}{L}{D*y}'
            #print(out, '\n')  
            out += '\n'
    return out
print(x(33))

def x1(n):
    # have fun ;)
    res = []
    for i in range(n // 2):
        res.append('□' * i + '■' + '□' * (n - 2 * i - 2) + '■' + '□' * i)
    res.append('□'*(n//2) + '■' + '□'*(n//2))
    for i in range(n // 2 + 1, 1, -1):
        res.append('□' * (i - 2) + '■' + '□' * (n - 2 * i + 2) + '■' + '□' * (i - 2))
    ans = ''.join([x +'\n' for x in res])
    return ans[:-1]



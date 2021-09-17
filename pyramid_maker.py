'''
Function takes number and return 0 =>[], 1 => [[1]], 2=> [[1], [1,1]], 3=>[[1], [1,1], [1,1,1]]
'''
#My solution
def pyramid(n):
    arr = []
    out = []
    for x in range (0, n):
        arr.append(1)
        print (arr)
    for y in range (0, n):   
        out.append(arr[y:n])
    out = out[::-1]
    
    return out



print(pyramid(3))


#Good solution
def pyramid(n):
    return [ [1] * i for i in range(1, n+1) ]


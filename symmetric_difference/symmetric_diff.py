def sym (set1, set2):
    tmp = set()                
    for x in set2:
        if x not in set1:
            tmp.add(x)
            print(tmp)    
    for y in set1:
        if y not in set2:
            tmp.add(y)
    out = list(tmp)            
    return out

print(sym ([1, 2, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3], [5, 2, 1, 4, 5]))
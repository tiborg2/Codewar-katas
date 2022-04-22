a = 'solo'
b = "soltenance"
dct_a = {}
dct_b = {}
for i in range(len(a)):
    if a[i] in dct_a:
        dct_a[a[i]] += 1
    else:
        dct_a[a[i]] = 1
for i in range(len(b)):
    if b[i] in dct_b:
        dct_b[b[i]] += 1
    else:
        dct_b[b[i]] = 1
count_1 = 0
for item in dct_a:
    if item in dct_a:
        count_1+=1


print (dct_a, '\n', dct_b)


'''
lst_a = list(a)
lst_b = list(b)
print (lst_a, lst_b)
for la in lst_a:
    if la in lst_b:
        lst_a.remove(la)
        lst_b.remove(la)
'''
#print(lst_a, '\n', lst_b)


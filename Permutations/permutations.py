import itertools as itr
def permutations(string):
    permutations = list(itr.permutations(string))
    out = list()
    for i in permutations:
        temp = str()
        for char in i:
            temp += char
        out.append(temp)
    return out
print(permutations("BDA"))


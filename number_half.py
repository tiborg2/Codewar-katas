def halving_sum(n):
    x = int(n)
    count = list()
    count.append (n)
    while x >= 1:
        y = int(x / 2)
        count.append(y)
        x = int(x / 2)
    return int(sum(count))
    
print(halving_sum(127))

# 247
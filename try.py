def isPrime(num1) :
    if (num1 <= 3) :
        return True
    if (num1 % 2 == 0 or num1 % 3 == 0) :
        return False
    i = 5
    while(i * i <= num1) :
        if (num1 % i == 0 or num1 % (i + 2) == 0) :
            return False
        i = i + 6
    return True
#print(isPrime(2))

S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
f = enumerate(S)
print(f['1'])





    
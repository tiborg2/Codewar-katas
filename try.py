def swicher(n):
        if n % 3 == 0 and n % 5 == 0:
            return "fizzbuzz"
        if n % 3 == 0:
            return "fizz"
        if n % 5 == 0:
            return "buzz"
        else:
            return "No buzz no fizz!"
print(swicher(7))



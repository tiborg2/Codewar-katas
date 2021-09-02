def swicher(n):
        if n % 3 == 0 and n % 5 == 0:
            return "fizzbuzz"
        if n % 3 == 0:
            return "fizz"
        if n % 5 == 0:
            return "buzz"
        else:
            return "No buzz no fizz!"
'''
n = 7
while n != 'q':
    if isinstance(n, int):
        print(n)
        #print(swicher(n))
        # return swicher(n)
        m = input("Please be so kind, insert number, or 'q' for quit: ")                        
    else:
        m = input("That was not number. Please be so kind, insert number, or 'q' for quit: ")
    n = m
    print (n)
print("Bye! Have a good time.")
'''
n = input("skaicius: ")
while n != 'q':
    if n.isdigit(): 
        m = int(n)
        print (n)
        m = input("ivesk kita skaiciu arba 'q': ")
    else:
        m = input("ne skaicius ivesk skaiciu arba 'q': ")
    n = m
print ("bye!") 

# print (swicher(m))

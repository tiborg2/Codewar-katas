'''
Fizz buzz is a group word game for children to teach them about division.
Players take turns to count incrementally, replacing any number divisible by three with the word "fizz",
 and any number divisible by five with the word "buzz". If number divisible for both return "fizzbuzz"
 Function gets number and answers 
'''
def fizz_buzz():
    def swicher (n):
        if n % 3 == 0 and n % 5 == 0:
            return "fizzbuzz"
        if n % 3 == 0:
            return "fizz"
        if n % 5 == 0:
            return "buzz"
        else:
            return "No buzz no fizz!"
    
    n = input("Please be so kind, insert number, or 'q' for quit: ")
       
    while n != 'q':
        if n.isdigit(): 
            m = int(n)
            print(swicher(m))
            # return swicher(n)                
            m = input("Please be so kind, insert number, or 'q' for quit: ")
        else:
            m = input("That was not number. Please be so kind, insert number, or 'q' for quit: ")
        n = m
    print("Bye! Have a good time.")

fizz_buzz()


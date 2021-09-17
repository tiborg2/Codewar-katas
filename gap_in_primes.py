from timeit import default_timer as timer

start = timer() 
def prime_search(dst, num, num2):
    
    def error_handler (dst, num, num2):
        if dst < 1:
            return None
        if num < 2:
            num = 2
        if num >= num2:
            return None
        out = num
        return out

    def is_prime(num1):#Checks if numbet is prime number.
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

    def is_distance(dst, prime_):#Finds requred distance between nearest prime numbers in given list 
        out = []
        for i in range(0, len(prime_lst)-1):
            if prime_lst[i+1] - prime_lst[i] == dst:
                out.append(prime_lst[i])
                out.append(prime_lst[i+1])
                return out        
        return None
    
    num1 = error_handler(dst, num, num2)
    if num1 == None:
        return None
    prime_set = set()
    for num1 in range (num1, num2+1): 
        if is_prime(num1):
            prime_set.add(num1)
    #print(prime_lst)
    prime_lst = tuple(sorted(prime_set))
    #print(prime_lst)
    out = is_distance(dst, prime_set)
    return out

    
   
print(prime_search(90, 100, 100000))
finish = timer()
print ("Execution time in ms:", (finish - start)*100)



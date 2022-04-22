'''
Function finds highest and lowest number in number list.
'''
def high_and_low(numbers):
    list1 = numbers.split()
    numbers = []
    for i in list1:
        x = int(i)
        numbers.append(x)  
    numbers.sort()
    out = f'{numbers[-1]} {numbers[0]}'

    return out
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
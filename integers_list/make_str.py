def while_next(args):
    args.append(-1000)
    big = []
    i = 0
    while i < len(args):
        if i < len(args) - 2:
            if (args[i]+1 == args[i+1]):
                small = []
                while (args[i]+1 == args[i+1]):
                    small.append(args[i])
                    i += 1
                big.append(small)
            big.append(args[i])
        else:
            if args[i] - 1 == args[i-1]:
                small.append(args[i])
                big.append(small)

            else:
                big.append(args[i])
        i += 1
    return big
        



# print (make_str(-1, 2))
print(while_next([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,26]))
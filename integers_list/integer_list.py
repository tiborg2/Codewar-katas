def solution(args):
    def make_str(digit, count):
        first = digit - count
        text = f"{first}-{digit}"
        return text
    rez = list()
    i = 0
    while i < len(args):
        if i < len(args)-1:
            count = 0
            while args[i]+1 == args[i+1]:
                count += 1
                if i < len(args) - 1:                
                    i += 1       
            if count > 0:
                rez.append(make_str(args[i+1], count))
            else:
                rez.append(args[i])
                i += 1
        else:
            rez.append(args[i])
            i += 1
        out = rez
    return out
     
print (solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20, 26]))
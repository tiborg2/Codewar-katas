'''Function builts ornament of size (x, y) 
(4,4) looks like this:

/**\
*  *
*  *
\**/

(1, 1) looks like this:

/

'''
def ornament (x, y):
    def error_handler(x, y):
        if isinstance(x, int) == False or isinstance(y, int) == False:
            print("Error: parameters are not digits.")
            return False
        if x < 1 or y < 1:
            print("Error: Parameters are too small.")
            return False
        return True
    def printer(x, y):
        out = ''
        for lin in range(1, y):
            for col in range(1, x):
                if col == 1 and lin == 1:
                    out += '/'
                    print (out)
                elif col > 1 and col < x and lin == 1:
                    out += '*'
                    print (out)
                elif col == x and lin == 1:
                    out += "\\"+"\n"
                    print (out)
                elif col == 1 and lin > 1 and lin < y:
                    out += '*'
                elif col == x and lin > 1 and lin < y:
                    out += '*'+"\n"
                elif col == 1 and lin == y:
                    out += "\\"
                elif col == x and lin == y:
                    out += "/"
                else:
                    out+= " "
            
            return out
    

                
    if error_handler(x , y) == False:
        return False
    else:
        out = printer(x, y)
    return out

ornament(4, 4)
    

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
        for lin in range(1, y+1):
            for col in range(1, x+1):
                if col == 1 and lin == 1:
                    out = '/'            
                elif col > 1 and col < x and lin == 1:
                    out += '*'            
                elif col == x and lin == 1:
                    out += "\\"+"\n"           
                elif (col == 1) and (lin > 1) and (lin < y):
                    out += '*'
                elif col == x and lin > 1 and lin < y:
                    out += '*'+"\n"
                elif col == 1 and lin == y:
                    out += "\\"
                elif col > 1 and col < x and lin == y:
                    out += "*"
                elif col == x and lin == y:
                    out += "/"
                else:
                    out+= " "
        return out

    if error_handler(x , y) == False:
        return "Program quit."       
    else:
        out = printer(x, y)
    return out
#Test line.
print(ornament(2, 'e'))
    

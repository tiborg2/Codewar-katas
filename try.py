def error_handler(x, y):
    if isinstance(x, int) == False or isinstance(y, int) == False:
        print("Error: parameters are not digits.")
        return False
    if x < 1 or y < 1:
        print("Error: Parameters are too small.")
        return False
    return True

print(error_handler(10, 1))

out = ''
out += "\\"+"\n" +'a'
print(out)
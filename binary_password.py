def decode_pass(pass_list:list, bits:str):
    #Finds binary coded info and checks in password list if it is correct password.
         
    binary_array = bits.split() # Split string on whitespace
    password = ""
    for char in binary_array:
        an_integer = int(char, 2) # Convert to base 2 decimal integer
        letter = chr(an_integer) # Convert to ASCII character
        password += letter # Append character to `ascii_string`
    if password in pass_list:
        return password
    else:
        return False

    
print(decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))


def decode_pass(pass_list, bits):
    s = "".join(chr(int(x, 2)) for x in bits.split())
    return s if s in pass_list else False
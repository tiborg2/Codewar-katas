def fake_bin(x:str) -> str:
    out = []
    for i in x:
        num = int(i)
        if num > 4:
            out.append('1')
        else:
            out.append('0')
    string = ''.join(out)       
    return string
print(fake_bin('366058562030849490134388085'))

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
    
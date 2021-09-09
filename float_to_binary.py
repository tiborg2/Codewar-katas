import struct
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))


def my_binary(num):
    var  = struct.pack('!f', num)

    return var





print(binary(15.875))
print(my_binary(15.875))
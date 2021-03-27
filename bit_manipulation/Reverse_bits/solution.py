# for easy explanation let us assume for 8 bits.
# a number N = 5 (00000101)
# on reversing 10100000 = 160


def reversing_bits(number):
    rev = 0
    for i in range(0,32): # for 32 bit
        temp = number & 1 
        reverse_lsb = temp << (31 - i )
        rev = rev | reverse_lsb
        number >>= 1
    return rev

# test case
number = 3
answer = reversing_bits(number)
print(answer)

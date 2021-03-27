
# Using Brain Kernighan 's Algorithm.(Explained below)
# subtracting 1 from a decimal number flip all the bits after the rightmost setbit including it.
#ex :7 = 111
#7-1=6 = 110
#6-1=5 = 101
#5-1=4 = 100...
# So , if we subtract number by 1 , and do bitwisee and with itself (n & n-1) ,we unset the rightmost set bit.
#If we does this is loop and count each time ,at the end we gonna get the total number of set bits.

# good thing about this algo is that it takes the time as total number of bits of number.
def count_setbits(number):
    count = 0
    while number :
        number = number & ( number - 1 ) 
        count += 1
    return count

# test case
number = 6
ans = count_setbits(number)
print(ans)
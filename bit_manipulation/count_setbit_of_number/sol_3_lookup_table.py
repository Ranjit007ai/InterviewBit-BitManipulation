# concept used here is quite simple and formulative i.e
# no of setbit of a number  = no of setbit of a Number//2 (If the number is EVEN)
# no of setbit of number = no of setbit of number //2 + 1 (IF number is ODD)
# i.e   ******* NO of setbit of number = no of setbit of number // 2  + number % 2   ***

# ex number = 6 (110)  number //2 = 3 (0,1,1) = 2 + 0 => 2

def count_setbit(number):
    # creating a lookup table (List) which will store no of set bit of all number upto the NUMBER.

    lookup_table = [0] * (number+1)        # initialize with 0 of size number 
    for i in range(1,number+1): # since the 0 index 0 = 000 no of set bit = 0 ,by default so starting from number 1 
        lookup_table[i] = lookup_table[i//2]  + (i % 2)
    return lookup_table[number]

# test case
number = 6
no_of_setbit = count_setbit(number)
print(no_of_setbit)

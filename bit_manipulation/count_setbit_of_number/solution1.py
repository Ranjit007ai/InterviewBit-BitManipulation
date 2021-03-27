# defining function to count total number of Setbits(1) in the given number.
# ex : number = 6 binary form->(110) ,there are 2 Setbit(1) in n = 6
# performing the right shift by 1 is same as Number // 2 ex : 6 :- 110 >> 1 = 011 = 3 .

# time complexity the while loop will run N//2 times (since >> 1 = number //2 )i.e O(N)

def count_setbits(number):
    count = 0

    while number != 0 :
        
        product = number & 1            #performing BitWise multiplication using & (ex : n= 6 & 1=> (110) & (001) = 000 => 0 )
        
        if product == 1 :
            
            count += 1
        
        number >>= 1 #Right shift by 1 position (ex: 110 >> 1 = 011 )

    return count

# test case
number = 6

total_setbits = count_setbits(number)

print(total_setbits)

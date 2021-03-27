# the array consist of interger,where every integer is repeated thrice except one integer ,we need to return that.
def single_number(Arr):

    n = len(Arr)
    ones = 0
    twos = 0
    for i in range(0,n):
        ones = (ones ^ Arr[i] ) & (~twos)
        twos = (twos ^ Arr[i]) & (~ ones)
    return ones

# test case
Arr = [1,2,4,3,3,2,2,3,1,1]
unique_number = single_number(Arr)
print(unique_number)
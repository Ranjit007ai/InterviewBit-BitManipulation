# given a array of integers ,we need to return the  minimum XOR value b/w pairs.

def min_xor(Arr):
    length = len(Arr)
    # sorting the Arr
    Arr.sort()
    mini_xor =  999999999999 # initializing the minimum xor_value by INT_MAX
    for i in range(length - 1):
        value = Arr[i] ^ Arr[ i + 1 ]
        mini_xor = min(mini_xor , value )
    return mini_xor

# test case
arr = [0,2,5,7]
min_value = min_xor(arr)
print(min_value)
# Our task is to find out that single number in the array in which every element is appeared twice except for one number.we need to return that.
# it is sure that there is one single number in the array.
def single_number(Arr):
    res = 0
    length = len(Arr)
    for i in range(length):
        res = res ^ Arr[i]
    return res

# test case
arr = [1,2,2,3,1]
unique_number = single_number(arr)
print(unique_number)
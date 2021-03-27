#  each element can appear atmost twice 
def removeduplicate(Arr):
    n = len(Arr)
    length = 2
    if n <= 2:  # if the size of arr is less than or equal to 2 ,then there is no chance of repeating more than twice
        return Arr
    for i in range(2,n):
        if Arr[i] != Arr[length - 2] or Arr[i] != Arr[length - 1]:
            Arr[length] = Arr[i]
            length += 1
    return Arr[:length]


# test case
arr = [1,1,1,2]
ans = removeduplicate(arr)
print(ans)
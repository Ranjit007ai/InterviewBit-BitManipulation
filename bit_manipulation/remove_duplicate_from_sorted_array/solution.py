def removeduplicate(Arr):
    length = len(Arr)
    j = 0
    for i in range(1,length):
        if Arr[i] != Arr[i-1]:
            Arr[j] = Arr[i]
            j += 1
    return Arr[:j+1]

# test case
Arr = [1,1,2]
ans = removeduplicate(Arr)
print(ans)
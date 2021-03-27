# we need to return the max series of the ones in the array of 0 and 1.
def max_ones(Arr):
    length = len(Arr)
    count = 0
    maxi = 0
    for i in range(0,length):
        if Arr[i] == 1 :
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0
    return count

Arr = [1,1,0,0,1,1,1,1]
ans = max_ones(Arr)
print(ans)

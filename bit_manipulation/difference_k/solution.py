# given a array of integer ,we need to find if there is any pair present such that difference of them is equal to given value.If yes return True
# else return False

def diff_k(Arr,value):
    Arr.sort()
    i = 0
    j = 1
    length = len(Arr)
    while i < length and j < length :
        diff = Arr[j] - Arr[i]
        if i != j and diff == value :
            return True
        elif diff < value :
            j += 1
        else:
            i += 1
    return False

Arr = [1,3,2,6]
value = 2
ans = diff_k(Arr,value)
print(ans)
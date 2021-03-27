# given an array of integers and a value , we need to remove all occurence of that value from array and return the no of element left in array 
# after operation.
# ex Arr = [4,1,1,3,1,2] value = 1 , o/p length = 3 ,[4,2,3]
def removeelement(Arr,value):
    j = 0
    n = len(Arr)
    for i in range(0,n):
        if Arr[i] != value :
            Arr[j] = Arr[i]
            j += 1
    return j

# test case
Arr = [4,1,1,2,1,3]
value = 1
ans = removeelement(Arr,value)
print(ans)
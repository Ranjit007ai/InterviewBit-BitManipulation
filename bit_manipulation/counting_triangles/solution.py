# Given a array of + integers , we need to find no fo triangle that can be formed with three different array element as three side of triangle.
# For triangle ,the sum of any two side must be greater than 3rd side.
# ex - [3,4,6] -> 3+4 > 6 , 4+6 > 3, 6+3 > 4 -> It is a triangle

def counttriangle(Arr):
    Arr.sort()

    length = len(Arr)
    count = 0

    for i in range(length - 1,0,-1):
        l = 0
        r = i - 1
        while ( l < r ):
            if Arr[l] + Arr[r] > Arr[i] :
                count += (r - l)
                r -= 1
            else:
                l += 1
    return count

# test case
Arr = [4,6,3,7]
ans = counttriangle(Arr)
print(ans) 
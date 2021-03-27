def sum_bit_different(Arr,n):
    ans = 0
    for i in range(0,32):
        count = 0
        for j in range(0,n):
            if ( ( Arr[j] & (1 << i)) ) :
                count += 1
        ans += (count * (n - count ) * 2)
    return ans

# test case
Arr= [2,7]
ans = sum_bit_different(Arr,2)
print(ans)
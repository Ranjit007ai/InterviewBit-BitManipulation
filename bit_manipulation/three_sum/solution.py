# Given an array of integers ,find the sum of three numbers so that the sum is nearest to the given target value.

def sum_of_three_no(Arr,target):

    Arr.sort()

    mini_diff = 99999999999
    mini_sum = 9999999999999
    length = len(Arr)


    for i in range(length-2):

        j = i + 1
        k = length - 1

        while j < k :

            sums = Arr[i] + Arr[j] + Arr[k]
            diff = abs( target - sums )

            if sums == target :
                return sums
            elif sums > target :
                
                if mini_diff > diff:
                    mini_diff = diff
                    mini_sum = sums
                k -= 1

            elif sums < target :

                if mini_diff > diff:
                    mini_diff = diff
                    mini_sum = sums
                j += 1

    return mini_sum

# test case
Arr = [-1,2,1,-4]
target = 1
ans = sum_of_three_no(Arr,target) 
print(ans)
# Given a array of integers ,we have to return all the unique triplets ,whose sum equal to ZERO.

def three_sum_zero(Arr):
    # Sorting the array
    Arr.sort()

    final_output_list = []
    length = len(Arr)
    for i in range(0,length - 2):
        j = i + 1
        k = length - 1
        while j < k :
            sums = Arr[i] + Arr[j]  + Arr[k]
            if sums == 0 :
                temp = [Arr[i],Arr[j],Arr[k]]
                if temp != final_output_list :
                    final_output_list.append(temp)
                
                k -= 1
                j += 1
            if sums > 0 :
                k -= 1
            else:
                j += 1
    return final_output_list

# test case
Arr = [-1,0,1,2,-1,-4]
output = three_sum_zero(Arr)
print(output)   
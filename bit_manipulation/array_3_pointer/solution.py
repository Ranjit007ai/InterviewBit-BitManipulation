# Given 3 sorted array A,B,C . we need to find i,j,k such that:
#max(abs(A[i] - B[j]),abs(B[j]- C[k]),abs(c[k] - A[i])) is minimum.

def minimize(A,B,C):
    diff = 99999999999999
    res_i , res_j, res_k = 0,0,0
    p = len(A)
    q = len(B)
    r = len(C)
    i,j,k = 0,0,0
    while i < p and j < q and k < r :
        # find minimum and maximum of current three element
        minimum = min(A[i],B[j],C[k])
        maximun = max(A[i],B[j],C[k])
        # update result if current diff is less than min_diff so far
        if maximum - minimum < diff :
            res_i = i
            res_j = j 
            res_k = k 
            diff = maximun - diff
        if diff == 0:
            break
        # increment index of array with smallest value
        if A[i] == minimum :
            i+= 1
        elif B[j] == minimum :
            j += 1
        else:
            k += 1
    return diff

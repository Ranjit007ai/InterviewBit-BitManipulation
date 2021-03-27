def max_series(Arr):
    string = ''
    for i in Arr:
        string += str(i)
    string = int(string)
    count = 0
    while string:
        string = string & (string << 1)
        count += 1
    return count

# test case
Arr = [1,1,0,0,1,1,1]
ans = max_series(Arr)
print(ans)
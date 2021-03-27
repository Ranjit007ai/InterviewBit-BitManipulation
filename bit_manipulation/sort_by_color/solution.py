# given a array of n object , consisting with color Red(0),White(1),Blue(2),we need to sort them such that same color come side to each other.

def sort(Arr):
    length = len(Arr)
    # let us count the total number of Red(0),White(1),Blue(2) color in the array.
    count_color_red = 0
    count_color_white = 0
    count_color_blue = 0
    for i in range(0,length):
        if Arr[i] == 0 : # if the color is Red
            count_color_red += 1
        elif Arr[i] == 1: # if the color is white
            count_color_white += 1
        else: # if the color is blue
            count_color_blue += 1
    # first the color red(0) will be there
    i = 0
    while count_color_red > 0:
        Arr[i] = 0
        i += 1
        count_color_red -= 1
    # Now for the color White(1)
    while count_color_white > 0:
        Arr[i] = 1
        i += 1
        count_color_white -= 1
    # Now for the color Blue
    while count_color_blue > 0 :
        Arr[i] = 2
        i += 1
        count_color_blue -= 1
    return Arr

# testcase
Arr = [0,2,1,0,2,2,1,1,0]
output_arr = sort(Arr)
print(output_arr)

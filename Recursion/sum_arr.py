# arr = [1,2,3,4]
def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr[0]
        rest = arr[1:]
        return first + sum_arr(rest)
    
print(sum_arr([4,5,7,8]))
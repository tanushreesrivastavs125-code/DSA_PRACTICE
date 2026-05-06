def permutation(arr):
    result = []

    def backtrack(index):
        if index == len(arr):
            result.append(arr[:])
            return
        for i in range(index,len(arr)):
            arr[index],arr[i] = arr[i],arr[index]

            backtrack(index+1)

            arr[index],arr[i] = arr[i],arr[index]

    backtrack(0)
    return result



print(permutation([1,2,3]))

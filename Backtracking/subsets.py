def subsets(arr):
    result = []
    def backtrack(index,current):
        result.append(current[:])

        for i in range(index,len(arr)):
            current.append(arr[i])

            backtrack(i+1,current)

            current.pop()

    backtrack(0,[])
    return result

print(subsets([1,2,3]))
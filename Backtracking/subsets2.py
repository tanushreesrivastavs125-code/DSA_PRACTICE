def subsets(arr):
    result = []
    arr.sort()

    def backtrack(index,current):
        result.append(current[:])

        for i in range(index,len(arr)):
            if i > index and arr[i] == arr[i-1]:
                continue
            else:
                current.append(arr[i])

                backtrack(i+1,current)

                current.pop()

    backtrack(0,[])
    return result

print(subsets([1,2,2]))
print(subsets([1,1,2,2]))
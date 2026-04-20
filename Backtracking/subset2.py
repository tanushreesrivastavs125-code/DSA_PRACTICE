# nums = [1,2,2]
# result = []

def subsets(nums):
    nums.sort()
    result = []

    def backtrack(index, current):
        result.append(current[:])

        for i in range(index, len(nums)):
            if i>index and nums[i] == nums[i-1]:
                continue
            else:
                current.append(nums[i])

                backtrack(i+1, current)

                current.pop()

    backtrack(0, [])
    return result
print(subsets([1,2,2]))
print(subsets([2,2,1,1]))
print(subsets([2,2]))
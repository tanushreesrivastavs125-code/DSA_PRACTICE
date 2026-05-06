def twoSum2(nums,target):
    left , rigth = 0 , len(nums)-1

    while left < rigth:
        sum = nums[left] + nums[rigth]

        if sum == target:
            return [left+1 , rigth+1]
        elif sum < target:
            left += 1
        else:
            rigth -= 1

print(twoSum2([2,4,6,8],10))
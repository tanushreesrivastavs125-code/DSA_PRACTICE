def subsets(arr,ans=[],i=0):
    if i == len(arr):
        ans.append(arr[i])
        return ans
    subsets(arr,ans,i+1)
    ans.pop()
    subsets(arr,ans,i+1)

print(subsets([1,2,3]))
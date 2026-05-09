def maxwater(height):
    left , right = 0 , len(height)-1

    max_area = 0

    while left < right:
        weidth = right-left
        current_height = min(height[left],height[right])

        area = weidth*current_height
        max_area = max(area,max_area)

        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    return max_area
print(maxwater([1,8,6,2,5,4,8,3,7]))
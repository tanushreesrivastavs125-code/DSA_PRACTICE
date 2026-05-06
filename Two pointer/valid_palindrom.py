# s = "A man, a plan, a canal: Panama"
def isPalindrom(arr):
    left , rigth = 0 , len(arr)-1

    while left < rigth:

        while left < rigth and not arr[left].isalnum():
            left += 1
        while left < rigth and not arr[rigth].isalnum():
            rigth -= 1
        if arr[left].lower() != arr[rigth].lower():
            return False
        
        left+=1
        rigth-=1

    return True
    
print(isPalindrom("A man, a plan, a canal: Panama"))
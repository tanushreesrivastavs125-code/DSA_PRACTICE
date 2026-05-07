def reverse(s):
    s = list(s)

    left , rigth = 0 , len(s)-1

    while left < rigth:
        s[left] , s[rigth] = s[rigth] , s[left]

        left += 1
        rigth -= 1

    return "".join(s)
    
print(reverse("tanushree"))
print(reverse("hello"))
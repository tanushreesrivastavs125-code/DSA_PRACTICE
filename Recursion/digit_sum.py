def digit_sum(n):
    if n < 10:
        return n
    else:
        s = n%10
        return s + digit_sum(n//10)
    
print(digit_sum(421))
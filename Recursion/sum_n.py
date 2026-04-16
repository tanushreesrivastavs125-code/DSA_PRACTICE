def sum_number(n):
    if n == 0:
        return 0
    else:
        return sum_number(n-1) + n
    
print(sum_number(5))

# TODO: x^n = 2^3

#  def power_ofnum(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * power_ofnum(x,n-1)

# print(power_ofnum(2,3))

# ? Time Limit Exceeded

def power_ofnum(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n<0:
        n = -n
        x = 1/x
    half = power_ofnum(x,n//2)
    if n%2 == 0:
        return half*half
    else:
        return x*half*half
    
print(power_ofnum(2,3))
print(power_ofnum(2,-3))

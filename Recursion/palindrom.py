
# TODO: wow , mam , dad , madam check if palindrom

#  def palindrom(name):
#     if len(name) == 0:
#         return "not a palindrom"
#     else:
#         def reverse_strr(name):
#             if len(name) == 0:
#                 return ""
#             else:
#                 return name[-1] + reverse_strr(name[:-1])
#     if reverse_strr(name) == name:
#         return "Palindrom"
#     else:
#         return "not a palindrom"
    
# print(palindrom("tanu"))
# print(palindrom("wow"))

# ? ISS ME MENE palindrom VALE RECUSION KA USE HI  NAHI KIYA

def palindrom(name):
    if len(name) <= 1:
        return True
    if name[0] != name[-1]:
        return False
    else:
        return palindrom(name[1:-1])
    
print(palindrom("tanu"))
print(palindrom("madam"))

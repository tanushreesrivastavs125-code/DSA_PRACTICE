
# TODO: tanu == rev(unat)

def reverse_strr(strr):
    if len(strr) == 0:
        return ""
    else:
        return strr[-1] + reverse_strr(strr[:-1])
    
print(reverse_strr("tanu"))
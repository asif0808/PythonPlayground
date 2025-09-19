#removing substring from given string without using replace()
def Remove_Sub(s,sub):
    i=0
    result=""
    while i<len(s):
        if s[i:i+len(sub)]==sub:
            i+=len(sub)
        else:
            result+=s[i]
            i+=1
    return result
print(Remove_Sub("Hello there , whats there","there"))
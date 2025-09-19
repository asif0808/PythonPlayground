#Write program to remove all occurence of substring from given string
def Remove_Sub(s,sub):
    s=s.replace(sub,"")
    return s
print(Remove_Sub("Hello there , whats there","there"))

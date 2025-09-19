#program to replace spaces in string with "%20"
def Replace_Space(s):
    s=s.replace(" ","%20")
    return s
print(Replace_Space("Hello how r u"))
#without replace()
def Replace_S(s):
    result=[]
    for i in s:
        if i==" ":
            result.append("%20")
        else:
            result.append(i)
    return "".join(result)
print(Replace_S("Hello this is me"))

#Encode a string (TYpical string compression)
def Encode_string(s):
    if not s:
        return ""
    encode=[]
    count=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            encode.append(s[i]+str(count))
            count=1
    # for last group
    encode.append(s[-1]+str(count))
    return ''.join(encode)
print(Encode_string("aaasssggg"))
def Decode_string(s):
    if not s:
        return ''
    decode=[]
    i=0
    while i<len(s):
        char=s[i]
        # print(char)
        num=""
        i+=1
        while i<len(s) and s[i].isdigit():
            # print(char)
            # print(i)
            num+=s[i]
            i+=1
            decode.append(char*int(num))
    return ''.join(decode)
print(Decode_string("a3d4"))
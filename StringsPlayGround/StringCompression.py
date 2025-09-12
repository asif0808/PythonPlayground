#write program to perform basic string compression
def String_compression(s):
    if not s:
        return ""
    result=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            result.append(s[i-1]+str(count) if count>1 else "")
            count=1
    #for last character
    result.append(s[i-1]+str(count) if count>1 else "")
    print(''.join(result))
String_compression("aaccbb")
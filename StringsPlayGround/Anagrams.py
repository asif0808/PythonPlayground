#check if two strings are anagrams or not
#two strings are anagrams if both contains same no. of and type of characters
def Anagrams(s1,s2):
    return sorted(s1.lower())==sorted(s2.lower())
print(Anagrams("Hello","lleho"))
print(Anagrams("silent","Listen"))

def Are_anagrams(s1,s2):
    freq={}
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1
    for i in s2:
        if i in freq.keys():
            freq[i]-=1
        else:
            return False
    for i in freq.values():
        if i!=0:
            return False
    return True
print(Are_anagrams("Listen".lower(),"Silent".lower()))
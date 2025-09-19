#Implement substring search without using find()
def Find_sub(s,sub):
    i=0
    while i<len(s):
        if s[i:i+len(sub)]==sub:
            return True
        i+=1
    return False
print(Find_sub("Hell World , World Hell","Hello"))
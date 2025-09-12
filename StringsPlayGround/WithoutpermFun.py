#find all possible permutations without using permutations()
def All_perms(s,ans=""):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        char=s[i]
        #remaining parts after excluding s[i]
        rem=s[:i]+s[i+1:]
        All_perms(rem,ans+char)
All_perms("hey")
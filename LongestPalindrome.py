#Find Longest palindrome substring
def Longest_palindrome(s):
    if not s or len(s)==1:
        return s
    start,end=0,0
    def Expand_from_center(left,right):
        while left>=0 and right <len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    for i in range(len(s)):
        l1,r1=Expand_from_center(i,i)  #for odd len palindrome
        l2,r2=Expand_from_center(i,i+1) #for even len palindrome
        if r1-l1>end-start:
            start,end=l1,r1
        if r2-l2>end-start:
            start,end=l2,r2
    return s[start:end+1]
print(Longest_palindrome("abbcdddc"))
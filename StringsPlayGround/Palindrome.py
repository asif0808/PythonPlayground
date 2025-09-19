#a given string is palindrome if string=rev_string
def IsPalindrome(s):
    if s==s[::-1]:
        return True
    return False

print(IsPalindrome("Hello"))
print(IsPalindrome("sahas"))
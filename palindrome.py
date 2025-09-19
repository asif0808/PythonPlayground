#check if a string is valid palindrome , ignore non-alphanumeric characters
def Is_palindrome(s):
    new_s=""
    for ch in s:
        if ch.isalnum():
            new_s+=ch          # new_s+=ch.lower()
    print(new_s)
    return new_s==new_s[::-1]
print(Is_palindrome("garag nongarag"))
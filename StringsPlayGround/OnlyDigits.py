#check if a string contains only digits
def Only_digits(s):
    return s.isdigit()
print(Only_digits("43h2"))
print(Only_digits(""))
print(Only_digits("432"))
#without built-in function
def Check_digits(s):
    nums="0123456789"
    if not s:
        return False
    for i in s:
        if i not in nums:
            return False
    return True
print(Check_digits("6703"))
print(Check_digits("670h3"))
print(Check_digits(" "))
print(Check_digits(""))
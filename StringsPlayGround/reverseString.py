# def rev_str(s):
#     return s[::-1]
# print(rev_str("Hello World"))
# using loop
def rev_str(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rev_str("hello world"))
#find first non-repeating character in a string
def First_Non_Repeating(s):
    for i in s:
        if s.count(i)==1:
            return i
print(First_Non_Repeating("HeHlloeok"))
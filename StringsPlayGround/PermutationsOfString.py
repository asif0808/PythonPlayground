#find all permutations of a given string
#Below code is for substring
#Difference between permutations and substring is permutations are all possible
# arrangements of the characters and substring is continuous part of string
# def All_Substrings(s):
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             print(s[i:j+1])
# All_Substrings("Hello")
#returning all permutations using permutations()
from itertools import permutations
def All_permutations(s):
    total_perms=0
    perms=permutations(s)
    for p in perms:
        total_perms+=1
        print(''.join(list(p)))
    print("Total_perms: ",total_perms)
All_permutations("Hello")

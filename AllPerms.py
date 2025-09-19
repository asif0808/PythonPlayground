from itertools import permutations
def All_perms(s):
    all_perms=permutations(s)
    for i in all_perms:
        print(''.join(i))
All_perms("Hello")
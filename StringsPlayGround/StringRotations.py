#check if two strings are rotations of each other
def Are_rotations(s1,s2):
    if len(s1)!=len(s2):
        return False
    # if s2 not in s1+s1:
    #     return False
    # return True
    # or 
    return s2 in s1+s1
print(Are_rotations("ehllo","llohe"))
print(Are_rotations("ehllo","lloeh"))
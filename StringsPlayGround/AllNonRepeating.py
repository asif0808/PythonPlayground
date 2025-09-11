#find all non-repeating character in a given string
def All_Non_Repeating(s):
    Non_repeatings=[]
    for i in s:
        if s.count(i)==1:
            Non_repeatings.append(i)
    return Non_repeatings
print(All_Non_Repeating("HelloH"))

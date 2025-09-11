#Remove all duplicates from given string
def remove_dupls(s):
    new_s=""
    for i in s:
        if i not in new_s:
            new_s+=i
    return new_s
print(remove_dupls("HeHllo"))

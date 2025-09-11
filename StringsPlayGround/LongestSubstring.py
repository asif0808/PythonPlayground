#find longest substring without repeating characters
def Substring(s):
    sub_without_rep=""
    longest_sub=""
    for i in s:
        if i not in sub_without_rep:
            sub_without_rep+=i
        else:
            #restart checking from next character
            sub_without_rep=sub_without_rep[sub_without_rep.index(i)+1:]+i
            # print(sub_without_rep)
        if len(sub_without_rep)>len(longest_sub):
            # print(longest_sub)
            longest_sub=sub_without_rep
    return longest_sub
print(Substring("Hellonewthinng"))
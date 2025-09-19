#convert the given string to title case(capitalize first letter of each word)
def To_title(s):
    return s.title()
print(To_title("hello there how are you"))
#without using title()
def Title_case(s):
    s_list=s.split()
    result=[]
    for word in s_list:
        result.append(word[0].upper()+word[1:].lower())
    print(result)
    return " ".join(result)
print(Title_case("Hello , tHere hOw aRe yoU"))

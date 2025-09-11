#count vowels and consonants in a given string'
def Vowels_Consonents(s):
    vowels="aeiouAEIOU"
    no_vowels=0
    no_consonents=0
    for i in s:
        if i in vowels:
            no_vowels+=1
        elif i==" ":
            continue
        else:
            no_consonents+=1
    return f"Vowels: {no_vowels} and Consonents: {no_consonents}"
print(Vowels_Consonents("Hello There"))


#group anagrams from a list of strings
def Group_Anagrams(data):
    anagrams={}
    for d in data:
        key=''.join(sorted(d))
        if key not in anagrams:
            anagrams[key]=[]
        anagrams[key].append(d)
    print (list(anagrams.values()) )   
Group_Anagrams(['hello','how','are','olleh','owh']) 
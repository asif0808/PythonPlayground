#find the frequency of characters in a given string
def characters_freq(s):
    freq={}
    for i in s:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1
    #to get highest frequency character
    highest_freq_character=max(freq,key=freq.get)
    return freq,highest_freq_character
print(characters_freq("Hello How"))

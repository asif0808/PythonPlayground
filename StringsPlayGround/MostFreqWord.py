#find most frequent word in the given string
def Most_freq_word(s):
    data=s.split()
    freq={}
    for d in data:
        if d in freq.keys():
            freq[d]+=1
        else:
            freq[d]=1
    freq_word=max(freq,key=freq.get)
    print(freq_word)
Most_freq_word("Hello this is me and this is it whats this")
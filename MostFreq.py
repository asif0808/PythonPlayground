def Most_freq_word(s):
    data=s.split()
    freq={}
    for i in data:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1
    return max(freq,key=freq.get)
print(Most_freq_word("Hello how are you , you doing good?"))
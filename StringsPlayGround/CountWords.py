#find number of words in a given sentence
def No_of_words(s):
    s_list=s.split()
    return len(s_list)
print(No_of_words("hello hi there , we"))
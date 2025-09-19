#python program to reverse each word in sentence while keeping word order
def Reverse_Words(sentence):
    sentence_list=sentence.split()
    result=[]
    for l in sentence_list:
        result.append(l[::-1])
    return ' '.join(result)
print(Reverse_Words("Hello there , how doing"))
    
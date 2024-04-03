def mergeAlternately(word1, word2):
    word_list=[]
    for i,j in zip(word1,word2):
        word_list.append(i)
        word_list.append(j)
    if len(word1)>len(word2):
        word=''.join(word_list)+word1[len(word2):]
    elif len(word2)>len(word1):
        word = ''.join(word_list) + word2[len(word1):]
    else:
        return ''.join(word_list)
    return word
print(mergeAlternately('abc','def'))
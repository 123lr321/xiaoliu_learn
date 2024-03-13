def mergeAlternately(word1, word2):
        list_word1=list(word1)
        list_word2 = list(word2)

        if len(word1)<=len(word2):
           for i in range(1,len(word1)*2+1,2):
              list_word1.insert(i,(list_word2[0]))
              del list_word2[0]
           list_word1+=list_word2
        else:
            for i in range(1,len(word2)*2+1,2):
                list_word1.insert(i,(list_word2[0]))
                del list_word2[0]
        word=str(list_word1)
        return  word
print(mergeAlternately('abc','defgkrun'))
word=''


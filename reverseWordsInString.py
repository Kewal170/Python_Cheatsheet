def reverseWordsInString(string):
    s = string.split()
    rev = []
    for i in s:
        rev.append(i[::-1])
    result = " ".join(rev)
    return result



string = "Kewal is reversing the words of this sentence"
print(reverseWordsInString(string))
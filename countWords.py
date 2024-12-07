string = "kewal is trying to count the words in this sentence"

def countWords(string):
    s = string.split()
    count = 0
    for word in s:
        count+=1
    return count
print(countWords(string))

#way2
res = len(string.split())
print(f"Length : {res}")
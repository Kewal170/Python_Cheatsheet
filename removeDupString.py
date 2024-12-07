string = "kewal is a super hero"
string = string.replace(" ","")
answer = ""
for char in string:
    if char not in answer:
        answer+=char

print(answer)
s = "kewal is hero"
d = "rahul is here"
s1 = "kewal hero is"

print(sorted(s.replace(" ","").lower()) == sorted(d.replace(" ","").lower()))
print(sorted(s.replace(" ","").lower()) == sorted(s1.replace(" ","").lower()))
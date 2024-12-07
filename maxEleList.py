list1 = [12,43,76,23,41,1]
# print(max(list1)) # way 1

#way 2
maxi = list1[0]
for i in range(len(list1)):
    if(maxi<list1[i]):
        maxi = list1[i]
print(maxi)
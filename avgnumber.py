def findAvg(num):
    total =sum(num)
    length = len(num)
    avg = total//length
    return avg

l = [12,34,64,1,23,12,41,4,2]
print(findAvg(l))
def sumofDigits(num):
    n1 = str(num)
    count = 0
    for i in n1:
        count+=int(i)
    return count

print(sumofDigits(12345))
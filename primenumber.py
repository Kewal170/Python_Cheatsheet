def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2,num//2):
            if num%i==0:
                return False
    return True

def totalPrime(num):
    answer = []
    for i in range(num):
        if prime(i):
            answer.append(i)
    return answer

user = int(input("Enter total number of prime number to find : "))
result = totalPrime(user)
print(result)
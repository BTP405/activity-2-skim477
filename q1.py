//seongjun
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [num for num in range(2, n+1) if isPrime(num)]

n = 5
print(getPrimeNumbers(n))


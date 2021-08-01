def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            prime = False
            break
    return prime



number = 6480

count = []

while i <= number:
    for j in range(2,number +1):
        if number % j == 0:
            number //= j
            count.append(j)
            break
    i += 1
print(count)

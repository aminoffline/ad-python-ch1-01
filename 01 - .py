
def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            prime = False
            break
    if prime == True:
        return n



"""
numbers = []
for i in range(0 , 3):
    numbers.append(int(input()))

end_data = {}
count = []

for number in numbers:
    print(count)
    i = 1
    while i <= number:
        for j in range(2 , number + 1):
            if number % j == 0:
                number //= j
                count.append(j)
                break
        i += 1
    count.sort()
    print(count , len(count))
    end_data[number] = [count,len(count)]
print(end_data)
"""
n = 678
number = n
c = []
for i in range(2,n+1):
    if n % i == 0:
        #n //= i
        c.append(i)

prime_divisor = map(is_prime,c)
prime_divisor = list(prime_divisor)
prime_divisor = filter(lambda x:x!=None,prime_divisor)
prime_divisor = list(prime_divisor)
prime_count = len(prime_divisor)
print(prime_divisor , prime_count)
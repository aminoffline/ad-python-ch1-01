def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            prime = False
            break
    return prime



number = 6480

count = []

for i in range(2,number+1):
    print(number)
    if number % i == 0:
        print(i)
        number = number // i
        #print(number)
        count.append(i)
        #print(count)
        if number == 1 :
            break

print(count)

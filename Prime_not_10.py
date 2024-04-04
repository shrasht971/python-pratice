#  display prime numbers from 3 to 30
print("Prime numbers from 3 to 30 are:")
for num in range(3, 31):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

import math

A = int(input())
B = int(input())

count = 0

for num in range(A, B + 1):
    if num < 2:
        continue
    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1

print(count)
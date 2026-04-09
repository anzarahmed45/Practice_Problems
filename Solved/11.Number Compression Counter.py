num = int(input())
count = 0

while num % 2 == 0:
    num //= 2
    count += 1

print(count)
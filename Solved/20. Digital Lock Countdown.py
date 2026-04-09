num = int(input())

while num >= 10:
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    num = s

print(num)
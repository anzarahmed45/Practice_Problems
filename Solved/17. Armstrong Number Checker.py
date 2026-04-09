num = int(input())
temp = num
sum_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_cubes += digit ** 3
    temp //= 10

print("YES" if sum_cubes == num else "NO")
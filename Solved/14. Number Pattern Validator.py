num = input()

valid = True
for i in range(len(num) - 1):
    if num[i] >= num[i + 1]:
        valid = False
        break

print("YES" if valid else "NO")
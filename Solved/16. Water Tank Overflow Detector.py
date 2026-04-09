n = int(input())
flows = list(map(int, input().split()))

capacity = 1000
total = 0

for i in range(n):
    total += flows[i]
    if total > capacity:
        print(i + 1)
        break
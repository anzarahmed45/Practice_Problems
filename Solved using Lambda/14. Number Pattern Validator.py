num = input()

result = lambda num: "YES" if all(num[i] < num[i+1] for i in range(len(num) -1)) else "NO"

print(result(num))
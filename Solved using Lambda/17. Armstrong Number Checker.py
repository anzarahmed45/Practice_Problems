num = input()

armstrong = lambda num: "YES" if int(num) == sum(map(lambda num: int(num)**3, num)) else "NO"

print(armstrong(num))
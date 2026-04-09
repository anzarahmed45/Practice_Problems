num = int(input())
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if rev == original:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
balance = int(input())
n = int(input())

for i in range(n):
    amt = int(input())
    if amt % 100 == 0 and balance >= amt:
        balance -= amt
        print("SUCCESS")
    else:
        print("FAILED")

print(balance)
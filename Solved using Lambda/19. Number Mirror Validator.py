num = input()

result = lambda num: "PALINDROME" if num == num[::-1] else "NOT PALINDROME"

print(result(num))
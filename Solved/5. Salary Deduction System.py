salary = int(input())
late = int(input())
absent = int(input())

deduction = 0

if late > 10:
    deduction += 0.10
elif late > 5:
    deduction += 0.05

if absent > 2:
    deduction += 0.05

final = salary - (salary * deduction)
print(int(final))
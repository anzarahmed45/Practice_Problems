marks = list(map(int, input().split()))

result = lambda marks: "FAIL" if any(mark < 35 for mark in marks) else ("DISTINCTION" if sum(marks)/5 >= 75 else "PASS")

print(result(marks))

sentence = input().lower()
count = 0

for ch in sentence:
    if ch in "aeiou":
        count += 1

print(count)
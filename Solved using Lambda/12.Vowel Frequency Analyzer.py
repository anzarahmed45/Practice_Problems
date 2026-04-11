sentence = input().lower()

count = sum(map(lambda ch: ch in "aeiou", sentence))

print(count)
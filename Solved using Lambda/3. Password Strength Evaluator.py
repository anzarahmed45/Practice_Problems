password = input()

has_digit = any(map(lambda ch: ch.isdigit(), password))
has_upper = any(map(lambda ch: ch.isupper(), password))

result = "STRONG" if len(password) >= 8 and has_digit and has_upper else "WEAK"

print(result)
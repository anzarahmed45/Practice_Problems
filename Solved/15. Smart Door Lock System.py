correct = input()

for i in range(3):
    attempt = input()
    if attempt == correct:
        print("ACCESS GRANTED")
        break
else:
    print("LOCKED")
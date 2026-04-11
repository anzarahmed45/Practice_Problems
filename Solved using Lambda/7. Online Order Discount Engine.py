amount = int(input())

discount = lambda amount: amount * 0.8 if amount >= 5000 else amount * 0.90 if amount >= 3000 else amount * 0.95 if amount >= 1000 else amount

print(int(discount(amount)))
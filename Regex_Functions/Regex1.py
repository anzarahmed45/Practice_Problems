import re

text = '''My phone number is 9876543210 and my backup number is 9123456780.
Order ID: 45678, Amount: ₹2500, Discount: 15%
CFO  NUMBER IS (999)-444-7777'''

patterns = "\(\d{3}\)-\d{3}-\d{4}|\d{10}"

matches = re.findall(patterns, text)
print(matches) 
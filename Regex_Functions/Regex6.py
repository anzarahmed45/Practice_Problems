import re

text = """The company's consolidated revenue for FY2023 Q1 was $4.85 billion.
In the previous quarter, FY2022 Q4, the revenue stood at $3.90 billion.The count is 4500.
Operating expenses increased by 12% compared to FY2022 Q3.
Net profit margin improved to 18% in FY2023 Q1.fy2030 Q4
The total assets reported were $25.6 billion as of March 31, 2023."""

patterns = "FY(\d{4} Q[1-4])[^\$]+ \$([\d\.]+)"

matches = re.search(patterns, text)
print(matches.groups())
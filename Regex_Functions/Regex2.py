import re
text = """
Item 2 Results of Operations and Financial Condition.
On April 2, 2026, Tesla, Inc. published the press release which is attached hereto as Exhibit 99.1 and is incorporated herein by reference.


Item 9 Financial Statements and Exhibits.
This information is intended to be furnished under Item 2.02 of Form 8-K and shall not be deemed “filed” for purposes of Section 18 of the
Securities Exchange Act of 1934, as amended (the “Exchange Act”), or incorporated by reference in any filing under the Securities Act of 1933, as
amended, or the Exchange Act as shall be expressly set forth by specific reference in such a filing.
"""

patterns = "Item \d ([^\n]*)"

matches = re.findall(patterns, text)
print(matches)
import re
log = "Located in Frankfurt region"
pattern = r"Frankfurt"
search = re.search(pattern, log)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
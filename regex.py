import re
line = "You are one lucky fox"
pattern = r"lucky"
match = re.search(pattern, line)
if match:
    print("Match Found")
else:
    print("No Match")
### Print all lines with error
paragh = """Error: This is bad
Success: This is ok
Error: Wrong syntax"""
pattern = r"Error:.*"
matches = re.findall(pattern, paragh)
for m in matches:
    print(m)
print(matches)
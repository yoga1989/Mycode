import re
line = "A quick brown fox jumps over a lazy dog"
pattern = r"brown"
replacement = "red"
newline = re.sub(pattern, replacement, line)
print(newline)
import re
line = "apples,oranges,bananas,grapes"
pattern = r","
sep = re.split(pattern, line)
print(sep)
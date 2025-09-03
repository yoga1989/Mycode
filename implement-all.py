import re
# 01-string-concat.py
string1 = "Example of"
string2 = "Concatenation"
print(string1 + " " + string2)
# 01-string-len.py
s1len = len(string1)
print("string1 length is: ", s1len)
#01-string-lowercase.py
lowercase = string1.lower()
uppercase = string1.upper()
print("lower case of string1 : " , str(lowercase))
print("Upper case of string1 : " , str(uppercase))
#01-string-replace.py
sentence = "Apples are Black"
replaced = sentence.replace("Black", "Red")
print(replaced)
#01-string-split.py
splitted = sentence.split()
count = 1
for split in splitted:
    print("Split", str(count) + ": " + split)
    count = count + 1
#01-string-strip.py
withspace = "          I am a sentence with unregulated space    "
stripped = withspace.strip().replace("unregulated" , "regulated")
print(stripped)
#01-string-substring.py
# find a substring
line = "A black camray with v2 Engine"
if "Engine" in line:
    print("Substring Engine found in line")
else:
    print("substring Engine not found")
#03-regex-findall.py
logfile = """Pass: Command executed successfully
Error: Out of memory
Pass: output saved to log file
Error: No space left on device"""
pattern = r"Error:.*"
find = re.findall(pattern, logfile)
if find:
    print("Errors found")
    for errorlog in find:
        print(errorlog)
else:
    print("No errors")
#03-regex-match.py
#match starting line
log = "Search for errors"
pattern = r"Search"
match = re.match(pattern, log)
if match:
    print("Match found :", match.group())
else:
    print("Match not found")
#03-regex-replace.py
# find and replace string using regex
log = "Apples are black"
pattern = r"black"
replacement = "red"
replace = re.sub(pattern, replacement, log)
print(replace)
# 03-regex-search.py
pattern = r"are"
search = re.search(pattern, log)
print(search)
if search:
    print("Search found :", search.group())
else:
    print("Search not found")
#03-regex-split.py
list = "files,dirs,data,mount,ipaddr"
pattern = r","
delimit = re.split(pattern, list)
if delimit:
    for content in delimit:
        print(content)
else:
    print("Invalid delimiter")

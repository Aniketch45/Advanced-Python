import re
str = "python is object orientd python language, pythoneasy to use"
pattern = re.compile("python")
matcher = re.finditer(pattern,str)
count = 0                                 
for m in matcher:
    count += 1
    print("Start index:", m.start())
    print("matched pattern", m.group())
    print("end index:", m.end())

print("python is occur", count,"times")
                                 
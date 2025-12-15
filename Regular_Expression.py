import re
str="Python is object orientd language, easy to use"
pattern=re.compile("Python")
matcher=pattern.finditer(str)
for m in matcher:
    print("Start index:",m.start())
    print("matched pattern",m.group())
    print("end index:",m.end())


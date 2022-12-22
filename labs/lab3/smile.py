import re

face = input()
regex = ""
for i in face:
    if i.isalnum():
        regex = regex + i
    else:
        regex = regex + "\\" + i
z = re.findall(regex,input())
print(len(z))
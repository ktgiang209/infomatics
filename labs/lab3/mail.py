import re

regex = r"[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]+"

z = re.findall(regex,input())

if len(z)==1:
    print("correct")
else:
    print("incorrect")

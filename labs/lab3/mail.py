import re

regex = r"[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]+"
text = input()
z = re.findall(regex,text)
if z[0] == text:
    print("correct")
else:
    print("incorrect")

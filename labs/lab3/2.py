import re

regex = r"[А-Я][а-я]+(?= [А-Я]\.[А-Я]\.)"
z = re.findall(regex,input())
z.sort()
for name in z:
    print(name)
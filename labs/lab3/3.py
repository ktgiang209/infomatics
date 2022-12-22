import re

a = input()
b = input()
c = input()

regex = r"К[б-й л-п с-я ]Р[б-й л-п с-я ]А"
z = re.findall(regex,input())
for word in z:
    print(word)
#8<(
import re

regex = r"8<\("

z = re.findall(regex,input())
print(len(z))
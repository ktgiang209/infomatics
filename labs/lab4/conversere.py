import re
import time

start_time = time.perf_counter()

input = open('schedule.json', 'r', encoding="utf-8")

text = input.read()
input.close()

line = re.findall(r'.+', text)

n = 1;m = 0
result = ""
for x in line:
    temp = re.findall(r"[^ ]+", x)
    for i in temp:
        for j in range(len(i)):
                if i[j] == "{":
                    if m == 1:
                        result = result + ("\n")*n + "- "
                    else:
                        result = result + ("\n")*n
                    n = 1
                elif i[j] == "}":
                    result = result + ("\n")*n
                    n = 0
                elif i[j] == "," and i[j-1]=="\"":
                    result = result + ("\n")*n + (chr)(9)*m
                elif i[j] == "," and i[j-1]=="}":
                    result = result + ("\n")*n
                elif i[j] == "\"" and result[len(result)-1]==":":
                    result = result + " "
                elif i[j] == "\"":
                    result = result + i[j].replace("\"","")
                elif i[j] == "[":
                    m = 1
                elif i[j] == "]":
                    m = 0
                else:
                    result = result + i[j] 
                    
output = open('toyaml.yaml', 'w', encoding="utf-8")
output.write(result)
output.close()

print(time.perf_counter() - start_time)
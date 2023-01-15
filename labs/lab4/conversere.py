import re
import time

start_time = time.perf_counter()

input = open('/Users/macpro16/Desktop/labs/lab4/schedule.json', 'r', encoding="utf-8")

text = input.read()
input.close()

line = re.findall(r'.+', text)

n = 1;m = 0;l=-1
result = ""
txt=""
for x in line:
    temp = re.findall(r"[^ ]+", x)
    for i in temp:
        txt = txt + i
for i in range(len(txt)):
    if txt[i] == "{":
        if m == 1:
            result = result + ("\n")*n + "- "
        else:
            result = result + ("\n")*n
        n = 1
        l = l+1
    elif txt[i] == "}":
        result = result + ("\n")*n
        n = 0
        l = l-1
    elif txt[i] == "," and txt[i-1]=="\"":
        if m > l:
            result = result + ("\n")*n + (chr)(9)*(m-1) + "- "
        else:    
            result = result + ("\n")*n + (chr)(9)*m
    elif txt[i] == "," and txt[i-1]=="}":
        result = result + ("\n")*n
    elif txt[i] == "," and txt[i-1]=="]":
        result = result + ("\n")*n + (chr)(9)*m
    elif txt[i] == "," and m > l:
        if txt[i+1] == "[":
            result = result + ("\n")*n + (chr)(9)*m 
        else:
            result = result + ("\n")*n + (chr)(9)*(m-1) + "- "
    elif txt[i] == ":" and txt[i+1]=="\"":
        result = result + ": "
    elif txt[i] == ":" and txt[i+1] == "[":
        result = result + ": "+ ("\n")*n + (chr)(9)*m 
    elif txt[i] == "\"":
        result = result + txt[i].replace("\"","")
    elif txt[i] == "[":
        m = m +1
        if txt[i+1] != "{":
            result = result +"- "
    elif txt[i] == "]":
        m = m - 1
    else:
        result = result + txt[i] 
                
output = open('/Users/macpro16/Desktop/labs/lab4/toyaml.yaml', 'w', encoding="utf-8")
output.write(result)
output.close()

print(time.perf_counter() - start_time)
import time

start_time = time.perf_counter()

input = open('/Users/macpro16/Desktop/labs/lab4/schedule.json', 'r', encoding='utf-8')

string = input.read().split('\n')
input.close()
n = 1
m = 0
l = -1

result = ""
result1 = ""
for i in string:
    result = result + i.replace(" ","")
for i in range(len(result)):
    if result[i] == "{":
        if m == 1:
            result1 = result1 + ("\n")*n + "- "
        else:
            result1 = result1 + ("\n")*n
        n = 1
        l = l+1
    elif result[i] == "}":
        result1 = result1 + ("\n")*n
        n = 0
        l = l-1
    elif result[i] == "," and result[i-1]=="\"":
        if m > l:
            result1 = result1 + ("\n")*n + (chr)(9)*(m-1) + "- "
        else:    
            result1 = result1 + ("\n")*n + (chr)(9)*m
    elif result[i] == "," and result[i-1]=="}":
        result1 = result1 + ("\n")*n
    elif result[i] == "," and result[i-1]=="]":
        result1 = result1 + ("\n")*n + (chr)(9)*m
    elif result[i] == "," and m > l:
        if result[i+1] == "[":
            result1 = result1 + ("\n")*n + (chr)(9)*m 
        else:
            result1 = result1 + ("\n")*n + (chr)(9)*(m-1) + "- "
    elif result[i] == ":" and result[i+1]=="\"":
        result1 = result1 + ": "
    elif result[i] == ":" and result[i+1] == "[":
        result1 = result1 + ": "+ ("\n")*n + (chr)(9)*m 
    elif result[i] == "\"":
        result1 = result1 + result[i].replace("\"","")
    elif result[i] == "[":
        m = m +1
        if result[i+1] != "{":
            result1 = result1 +"- "
    elif result[i] == "]":
        m = m - 1
    else:
       result1 = result1 + result[i] 

output = open('/Users/macpro16/Desktop/labs/lab4/yamlschedule.yaml','w', encoding='utf-8')
output.write(result1)
output.close()

print(time.perf_counter() - start_time)

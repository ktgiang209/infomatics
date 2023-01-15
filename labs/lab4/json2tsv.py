input = open('/Users/macpro16/Desktop/labs/lab4/schedule.json','r', encoding='utf-8')
text = input.read()
input.close()

writing = False
element = True
result = {}
Result = ""
keys = []
n = 0
txt = ""
txt1 = ""

for i in text:
    if writing:
        if i == '"':
            writing = not writing
            if not element:
                result[txt].append(txt1)
                if len(result[txt]) > n:
                    n = len(result[txt])
                txt = ""
            else:
                if txt not in result:
                    result[txt] = []
                    keys.append(txt)
                txt1 = ""
            element = not element
            continue 
        if not element:
            txt1 += i
        else:
            txt += i
    else:
        if i == '"':
            writing = True
        elif i == "{":
            element = True
            txt = ""
Result = "\t".join(keys) + "\n"
for i in range(n):
    for key in keys:
        if (i < len(result[key])):
            Result += result[key][i]
        Result += "\t"
    Result += "\n"

output = open('/Users/macpro16/Desktop/labs/lab4/schedule.tsv','w', encoding='utf-8')
output.write(Result)
output.close()

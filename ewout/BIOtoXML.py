with open ("test.bio", "r", encoding="utf-8") as f:
    data = f.readlines()
    output = ""
    for line in data:
        try:
            line = line.split()
            if line[-1] != "O":
                line = "<" + line[-1] + ">" + line[0] + "</" + line[-1] + ">"
            else:
                line = line[0]
            output += line + " "
        except:
            output += "\n"

    x = output.count("<I-")
    x += 1
    while x >0:
        try:
            tag = output.index("<I-")
            tag = str(output[tag-9:tag+7])
            output = output.replace(tag, " ")
            x -= 1
        except:
            break

with open("test.xml", "w", encoding="utf-8") as p:
    p.write(output.replace(" .", ".").replace("B-", "").replace("I-", ""))



"""
Alex Brandsen, [2/22/2023 10:25 AM]
output = ""
for line in document:
split line
get token, get label
if label[:2] == "B-":
output += "<" + label[2:] + ">" + token + " "

current_entity = label[2:]
elif current_entity and  label[:2] != "I-":
output += token + " </" + label[2:] + ">" + " " 
else:
output += token + " "
"""
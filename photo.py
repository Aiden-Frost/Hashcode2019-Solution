fr = open("C:\\Users\\Rahul\\Desktop\\Studies\\Hash Code\\d_pet_pictures.txt","r")
fw = open("d_ouput.txt","a")
n = int(fr.readline())
dataV = {}
dataH = {}
for i in range(n):
    s = fr.readline()
    if s[0] == "V":
        dataV[i] = s.split()[2:]
    else:
        dataH[i] = s.split()[2:]
listV = list(dataV.items())
finalV ={}
while (len(listV)!=0):
    data = listV[0]
    match = listV[1]
    count = len(set(set(data[1]).intersection(set(match[1]))))
    listV.pop(0)
    j = 0
    while j<len(listV):
        match1 = listV[j]
        count1 = len(set(set(data[1]).intersection(set(match1[1]))))
        if count1>count:
            match = match1
        j+=1
    finalV[(match[0]),data[0]] = list(set(match[1]).union(set(data[1])))
    listV.remove(match)
data = {**dataH,**finalV}
final_data = list(data.items())
n = len(final_data)
fw.write(str(n)+'\n')
previous = final_data[0]
if type(previous[0]) is int:
    fw.write(str(previous[0])+'\n')
else:
    fw.write(str(previous[0][0])+' '+str(previous[0][1])+'\n')
final_data.pop(0)
while (len(final_data)!=0):
    data = previous
    match = final_data[0]
    count = len(set(set(data[1]).intersection(set(match[1]))))
    #final_data.pop(0)
    j = 0
    while j<len(final_data):
        match1 = final_data[j]
        count1 = len(set(set(data[1]).intersection(set(match1[1]))))
        if count1>count:
            match = match1
        j+=1
    if type(match[0]) is int:
        fw.write(str(match[0])+'\n')
    else:
        fw.write(str(match[0][0])+' '+str(match[0][1])+'\n')
    final_data.remove(match)
    previous = match
fw.close()
fr.close()
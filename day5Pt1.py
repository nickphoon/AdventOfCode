import numpy as np
def split():
    data = np.loadtxt("day5.txt", dtype='str')
    sect1, sect2 = {}, []
    for i in data:
        if("," in i):
            i = i.split(",")
            sect2.append(i)
        else:
            a,b = i.split("|")
            if a not in sect1:
                sect1[a] = [b]
            else:
                sect1[a].append(b)
    
    return sect1, sect2

def search():
    sect1, sect2 = split()
    count = 0
    for row in sect2:
        corr = True
        length = len(row)
        mid = length//2
        for index in range(length):
            if(index == length-1):
                break
            for num in row[index+1:]:
                if row[index] not in sect1:
                    # print(num, row)
                    corr = False
                elif(num not in sect1[row[index]]):
                    corr = False
        if corr:
            print(row[mid])
            count+=int(row[mid])
    
    return count

print(search())
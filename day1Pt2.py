with open("day1.txt") as file:
    list1, list2= [],[]
    for index, i in enumerate(file):
        ls = i.split()
        list1.append(ls[0])
        list2.append(ls[1])
    
list1 = sorted(list1)
list2 = sorted(list2)

dic = {}
dist = 0
for n1 in list1:
    if n1 in list2:
        if n1 not in dic:
            dic[n1] = 0
            for n2 in list2:
                if n1 == n2:
                    dic[n1] +=1
        score = (int)(n1) * dic[n1]
        dist += score


print(dist)
        
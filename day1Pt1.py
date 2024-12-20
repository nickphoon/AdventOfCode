with open("day1.txt") as file:
    list1, list2= [],[]
    for index, i in enumerate(file):
        ls = i.split()
        list1.append(ls[0])
        list2.append(ls[1])
    
list1 = sorted(list1)
list2 = sorted(list2)

dist = 0
for num1, num2 in zip(list1,list2):
    dist += abs(int(num1)-int(num2))

print(dist)
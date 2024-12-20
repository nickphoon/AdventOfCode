with open("day2.txt") as file:
    lines = file.read().strip().split("\n")
    count = 0
    for line in lines:
        ls = line.split()
        
        increase = int(ls[1]) > int(ls[0])
        length = len(ls)
        if increase:
            for num in range(1, length):
                diff = int(ls[num]) - int(ls[num-1])
                if not 1 <= diff <= 3:
                    count += 1
                    break
        else:
            for num in range(1, length):
                diff = int(ls[num]) - int(ls[num-1])
                if not -3 <= diff <= -1:
                    count += 1
                    break
            
print(len(lines) - count)
        
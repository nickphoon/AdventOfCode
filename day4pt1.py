import numpy as np

def checker(row, position, direction, test, rowLength, colLength):
    word_len = 4
    if direction == "Backward":
        if position - word_len + 1 < 0:
            return 0
        for i in range(word_len):
            if File_data[row][position - i] != test[i]:
                return 0
        return 1
    if direction == "Forward":
        if position + word_len > rowLength:
            return 0
        for i in range(word_len):
            if File_data[row][position + i] != test[i]:
                return 0
        return 1
    if direction == "Downward":
        if row + word_len > colLength:
            return 0
        for i in range(word_len):
            if File_data[row + i][position] != test[i]:
                return 0
        return 1
    if direction == "Upward":
        if row - word_len + 1 < 0:
            return 0
        for i in range(word_len):
            if File_data[row - i][position] != test[i]:
                return 0
        return 1
    if direction == "DDL":
        if row + word_len > colLength or position - word_len + 1 < 0:
            return 0
        for i in range(word_len):
            if File_data[row + i][position - i] != test[i]:
                return 0
        return 1
    if direction == "DDR":
        if row + word_len > colLength or position + word_len > rowLength:
            return 0
        for i in range(word_len):
            if File_data[row + i][position + i] != test[i]:
                return 0
        return 1
    if direction == "DUR":
        if row - word_len + 1 < 0 or position + word_len > rowLength:
            return 0
        for i in range(word_len):
            if File_data[row - i][position + i] != test[i]:
                return 0
        return 1
    if direction == "DUL":
        if row - word_len + 1 < 0 or position - word_len + 1 < 0:
            return 0
        for i in range(word_len):
            if File_data[row - i][position - i] != test[i]:
                return 0
        return 1
    return 0


File_data = np.loadtxt("day4.txt", dtype='str') 
def cool():
    count = 0
    txt = "XMAS"
    rowLength = len(File_data[0])
    colLength = len(File_data)
    directions = ["Forward", "Backward", "Upward", "Downward", "DDL","DDR","DUL","DUR"]
    for i,row in enumerate(File_data):
        for index,letter in enumerate(row):
            
            if(letter == "X"):
                    
                for dir in directions:
                    count += checker(i,index,dir,txt, rowLength, colLength)
    return count       
    
x =cool()
print(x)




    
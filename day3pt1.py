import re

res = 0
def multiply(str):
    str.split()

with open("day3.txt") as file:
    for i in file:
        # ls = i.split("mul")
                # Regular expression to match substrings starting with "mul(x,y)"
        
        pattern = r"mul\((\d+),(\d+)\)"
        # new = re.findall(newPattern,i)
        
        # Find all matches
        # Extract the (x, y) pairs as tuples of integers
        matches = [(int(x), int(y)) for x, y in re.findall(pattern, i)]

        # Calculate the sum of the multiplications
        tempSum = sum(x * y for x, y in matches)
        res += tempSum

print(res)
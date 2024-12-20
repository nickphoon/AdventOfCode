import re

# Initialize the result variable
res = 0

# Open the file and process each line
with open("day3.txt") as file:
    for line in file:
        # Split the line based on "don't()" and "do()"
        before_dont, _, after_do = line.partition("don't()")

        # Process the part before "don't()"
        pattern = r"mul\((\d+),(\d+)\)"  # Match mul(x, y)
        matches_before = [(int(x), int(y)) for x, y in re.findall(pattern, before_dont)]

        # Process the part after "do()"
        after_do = after_do.split("do()")[-1]  # Take everything after "do()"
        matches_after = [(int(x), int(y)) for x, y in re.findall(pattern, after_do)]

        # Calculate the sum of multiplications for both parts
        temp_sum_before = sum(x * y for x, y in matches_before)
        temp_sum_after = sum(x * y for x, y in matches_after)

        # Add to the total result
        res += temp_sum_before + temp_sum_after

# Print the final result
print(res)

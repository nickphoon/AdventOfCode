def is_safe(report):
    return is_increasing(report) or is_decreasing(report)


def is_increasing(report):
    """
    Check if all levels are increasing with valid differences (1 to 3).
    """
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff < 1 or diff > 3:
            return False
    return True


def is_decreasing(report):
    """
    Check if all levels are decreasing with valid differences (1 to 3).
    """
    for i in range(1, len(report)):
        diff = report[i - 1] - report[i]
        if diff < 1 or diff > 3:
            return False
    return True


def can_be_safe_with_one_removal(report):
    """
    Check if the report can be made safe by removing one level.
    """
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports(filename):
    """
    Count the number of safe reports from the file.
    """
    safe_count = 0

    # Read the file
    with open(filename, 'r') as file:
        for line in file:
            # Parse each report as a list of integers
            report = list(map(int, line.strip().split()))
            
            # Check if the report is safe or can be made safe
            if is_safe(report) or can_be_safe_with_one_removal(report):
                safe_count += 1

    return safe_count


# Main execution

filename = "day2.txt"
safe_count = count_safe_reports(filename)
print(f"Number of safe reports: {safe_count}")

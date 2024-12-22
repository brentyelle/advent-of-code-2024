def process_file(filename : str):
    reports = []
    with open(filename, 'r') as f:
        for line in f:
            reports.append([int(x) for x in line.split()])
    return reports

def is_safe(report):
    is_increasing = True
    is_decreasing = True
    is_not_steep  = True
    for i in range(len(report)):
        if i > 0:
            diff = report[i] - report[i-1]
            is_decreasing = is_decreasing and (diff < 0)
            is_increasing = is_increasing and (diff > 0)
            is_not_steep  = is_not_steep  and (0 < abs(diff) <= 3)
        if not((is_decreasing or is_increasing) and is_not_steep):
            return False
    return True

def is_dampened_safe(report):
    # classic-safe is still safe
    if is_safe(report):
        return True
    # otherwise, check if it's dampened-safe
    for i in range(len(report)):
        # check each slice with element of index `i` removed
        if is_safe(report[:i] + report[i+1:]):
            return True
    # if no safe slices found, it's fully unsafe
    return False

def main1(filename : str):
    reports = process_file(filename)
    safe_reports = list(filter(is_safe, reports))
    print(f"{filename}, part 1: {len(safe_reports)=}")

def main2(filename : str):
    reports = process_file(filename)
    safe_reports = list(filter(is_dampened_safe, reports))
    print(f"{filename}, part 2: {len(safe_reports)=}")

main1("day02test.txt")
main2("day02test.txt")
main1("day02input.txt")
main2("day02input.txt")
def process_file(filename : str) -> tuple[list[int], list[tuple[int,int]]]:
    """Imports all ordering rules as-is as a list strings of the format `xx|yy`.\n
    Imports all page requests as a list of lists of pages (as `int`s)."""
    ordering_rules  = []
    page_requests   = []
    with open(filename, 'r') as f:
        # miniature state machine to control if we're reading rules or page requests
        is_reading_rules = True
        for line in f:
            strippedline = line.strip()
            # once we find a blank line, switch from reading rules to requests
            if strippedline == "":
                is_reading_rules = False
                continue
            if is_reading_rules:
                # rules will stay as strings of the form "xx|yy"
                ordering_rules.append(strippedline)
            else:
                # requests will become lists of integers
                page_requests.append([int(x) for x in strippedline.split(',')])
    return ordering_rules, page_requests

def is_correct_order(request: list[int], rule_list: list[tuple[int,int]]) -> bool:
    """Determines if the request `request` is in the proper order according to the rules in `rule_list`.\n
    If a pair of numbers is not listed anywhere in `rule_list`, the pairing is not subject to any ordering restrictions."""
    # Compare each element to all elements that follow it.
    for i in range(0, len(request)-1):
        for j in range(i, len(request)):
            reverse_rule = str(request[j]) + '|' + str(request[i])
            # We don't need a rule *for* this order, but if there *is* a rule for the *opposite* order, that's no good.
            if reverse_rule in rule_list:
                return False
    return True

def make_correct_order(request: list[int], rule_list: list[tuple[int,int]]) -> list[int]:
    """Creates a new request by re-ordering the input `request` according to the rules in `rule_list`."""
    # We're going to make a new request that is the ordered version of the given `request`.
    request_copy = request[:]
    # Compare each element to all elements that follow it.
    for i in range(0, len(request_copy)-1):
        for j in range(i, len(request_copy)):
            reverse_rule = str(request_copy[j]) + '|' + str(request_copy[i])
            # We don't need a rule *for* this order, but if there *is* a rule for the *opposite* order, that's no good.
            # Swapping the elements to make them in order will implement BubbleSort.
            if reverse_rule in rule_list:
                request_copy[i], request_copy[j] = request_copy[j], request_copy[i]
    return request_copy

def main1(filename):
    rules, requests     = process_file(filename)
    correct_requests    = [r for r in requests if is_correct_order(r, rules)]
    center_numbers      = [r[len(r)//2] for r in correct_requests]
    print(f"{filename}, part 1: {sum(center_numbers)=}, there were {len(center_numbers)} correct requests")

def main2(filename):
    rules, requests     = process_file(filename)
    corrected_requests  = [make_correct_order(r, rules) for r in requests if not is_correct_order(r, rules)]
    center_numbers      = [r[len(r)//2] for r in corrected_requests]
    print(f"{filename}, part 2: {sum(center_numbers)=}, there were {len(center_numbers)} incorrect requests now fixed")

main1("day05test.txt")
main2("day05test.txt")
main1("day05input.txt")
main2("day05input.txt")
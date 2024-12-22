import re

def process_file(filename : str) -> str:
    reports = ""
    with open(filename, 'r') as f:
        reports = f.read()
    return reports

def evaluate_mul(mulstring : str) -> int:
    """Turn a string `"mul(x,y)"` into the product of `x` and `y`."""
    factor1, factor2 = mulstring.split(',')
    factor1 = int(factor1[4:])  # trim off the initial `mul(`
    factor2 = int(factor2[:-1]) # trim off the final `)`
    return factor1 * factor2

def find_muls(charstream : str) -> list[int]:
    """Find all instances of `"mul(x,y)"` in the string, then evaluate each one's multiplications."""
    REGEX_INSTANCE_OF_MUL = r"mul\(\d{1,3},\d{1,3}\)"
    return [evaluate_mul(mulstr) for mulstr in re.findall(REGEX_INSTANCE_OF_MUL, charstream)]

def find_muls_with_do(charstream : str) -> list[int]:
    """Go through the string finding all instances of `"mul(x,y)"`, then conditionally evaluate each one's multiplications.\n
    However, the `mul`s are evaluated in order: the command `don't()` disables any `mul`s from counting, while `do()` re-enables them."""
    REGEX_INSTANCE_OF_MUL   = r"mul\(\d{1,3},\d{1,3}\)"
    REGEX_INSTANCE_OF_DO    = r"do\(\)"
    REGEX_INSTANCE_OF_DONT  = r"don't\(\)"
    FULL_REGEX              = REGEX_INSTANCE_OF_MUL + r"|" + REGEX_INSTANCE_OF_DO + r"|" + REGEX_INSTANCE_OF_DONT
    prelim_results = re.findall(FULL_REGEX, charstream)
    true_results   = []
    # make a miniature state machine: if `should_do` is `True`, then evaluate the `mul(x,y)`, otherwise ignore it (here achieved by adding `0`)
    should_do = True
    for r in prelim_results:
        match r:
            case "do()":    # encountering `do()` enables evaluation of `mul(x,y)` expressions
                should_do = True
            case "don't()": # encountering `don't()` disables evaluation of `mul(x,y)` expressions
                should_do = False
            case _:         # otherwise this is a `mul(x,y)`, so add its value if `should_do` is currently `True`
                true_results.append(evaluate_mul(r) if should_do else 0)
    return true_results

def main1(filename : str):
    results = find_muls(process_file(filename))
    print(f"{filename}, part 1: {sum(results)=}")

def main2(filename : str):
    results = find_muls_with_do(process_file(filename))
    print(f"{filename}, part 2: {sum(results)=}")

main1("day03test1.txt")
main2("day03test2.txt")
main1("day03input.txt")
main2("day03input.txt")
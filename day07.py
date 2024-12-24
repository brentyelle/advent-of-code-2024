import itertools

OPERATORS1 = "+*"   # part 1
OPERATORS2 = "+*|"  # part 2

def process_file(filename : str) -> list[tuple[int, tuple[int]]]:
    """Each line of the input file is of the form `l: r1 r2 ... rN`.\n
    This function puts all `l`s in `leftsides`, and all lists of `r`s in `rightsides`."""
    leftsides  = []
    rightsides = []
    with open(filename, 'r') as f:
        for line in f:
            l, rs = line.strip().split(':')
            leftsides.append(int(l))
            rightsides.append([int(x) for x in rs.split()])
    return leftsides, rightsides

def evaluate_list(right_elems, operator_list):
    """Evaluates the expression with elements in `right_elems` and infix operators in `operator_list`.\n
    As instructed, the expressions are evaluated left-to-right, not following usual order of operations."""
    accumulator = right_elems[0]
    for i in range(len(operator_list)):
        match operator_list[i]:
            case '+':
                accumulator += right_elems[i+1]
            case '*':
                accumulator *= right_elems[i+1]
            case '|':
                # concatenation operator
                accumulator = int(f"{accumulator}{right_elems[i+1]}")
    return accumulator

def main(filename, *, part):
    """Given all of the sums/products in `lefts` and the lists of addends/factors in `rights`, searches for combinations of operators that can make the equation true. If a working combination is found, the sum/product is added to a running total `calibration_sum`. Finally, the total `calibration_sum` is printed.\n
    * Part 1: The operators are + (addition) and * (multiplication).\n
    * Part 2: The operators are + (addition), * (multiplication), and | (concatenation)."""
    lefts, rights   = process_file(filename)
    calibration_sum = 0
    for l, rs in zip(lefts, rights):
        combination_found = False
        # get all combinations of operators that could be in this equation
        operator_combos = itertools.product(OPERATORS1 if part==1 else OPERATORS2, repeat=len(rs)-1)
        for combo in operator_combos:
            if l == evaluate_list(rs, combo):
                # we only need to find one working combination for any given equation
                combination_found = True
                break
        if combination_found:
            calibration_sum += l
    print(f"{filename}, part {part}: {calibration_sum=}")

main("day07test.txt", part=1)
main("day07test.txt", part=2)
main("day07input.txt", part=1)
main("day07input.txt", part=2)
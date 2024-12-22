from collections import Counter

def process_files(filename : str):
    l_list   = []
    r_list  = []
    with open(filename, 'r') as f:
        for line in f:
            linesplit = line.split(" ")
            l_list.append(int(linesplit[0 ]))
            r_list.append(int(linesplit[-1]))
            # print(l_list, r_list)
    return l_list, r_list

def main1(filename : str):
    lefts, rights   = process_files(filename)
    lefts.sort()
    rights.sort()
    distances       = [abs(lefts[i] - rights[i]) for i in range(len(lefts))]
    total_dist      = sum(distances)
    print(f"{filename}, part 1: {total_dist=}")
    return

def main2(filename : str):
    lefts, rights   = process_files(filename)
    # occurences      = [rights.count(x) for x in lefts]
    occurences      = Counter(rights)
    similarities    = [x * occurences[x] for x in lefts]
    print(similarities)
    total_sims      = sum(similarities)
    print(f"{filename}, part 2: {total_sims=}")

main1(filename="day01test.txt")
main2(filename="day01test.txt")
main1(filename="day01input.txt")
main2(filename="day01input.txt")
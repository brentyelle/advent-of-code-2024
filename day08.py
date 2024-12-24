import numpy as np
import functools

def process_file(filename : str) -> np.ndarray:
    """Reads the file as a 2D `numpy` array of characters.\n
    Trailing whitespace is trimmed before conversion."""
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
    return np.array(lines)

def find_nodes(grid : np.ndarray) -> tuple[dict[str, set[tuple[int, int]]], set[tuple[int,int]]]:
    node_labels = [x for x in np.unique(grid) if x != '.']
    node_dict   = dict()
    node_points = set()
    for label in node_labels:
        # we use a `set` because each location either is or isn't an antinode; multiplicity is irrelevant
        node_dict[label] = {(i,j) for i,j in np.argwhere(grid == label)}
        node_points.update(node_dict[label])
    return node_dict, node_points

def find_antinodes(grid : np.ndarray, node_dictionary : dict[str, set[tuple[int, int]]], depth : int) -> set[tuple[int, int]]:
    HEIGHT = grid.shape[0]
    WIDTH  = grid.shape[1]
    antinodes  = set()
    # we don't need the keys, but we need the values grouped by key, hence why we use a dict
    for position_list in node_dictionary.values():
        # pair off `each` with every other position in the same `position_list`
        # (this is highly redundant, but our input is small enough that it doesn't matter)
        for position1 in position_list:
            p1 = np.array(position1)
            for position2 in position_list.difference({position1}):
                p2    = np.array(position2)
                delta = p2 - p1
                for n in range(1, depth+1):
                    antinodes.add(tuple(p1 - n*delta))
                    antinodes.add(tuple(p2 + n*delta))
    # filter out all the antinodes that are out-of-bounds
    return {(i,j) for i,j in antinodes if 0 <= i < HEIGHT and 0 <= j < WIDTH}

def main1(filename):
    antenna_grid        = process_file(filename)
    node_dict, _        = find_nodes(antenna_grid)
    antinodes           = find_antinodes(antenna_grid, node_dict, depth=1)
    print(f"{filename}, part 1: {len(antinodes)=}")

def main2(filename):
    antenna_grid        = process_file(filename)
    node_dict, node_pts = find_nodes(antenna_grid)
    antinodes           = find_antinodes(antenna_grid, node_dict, depth=50).union(node_pts)
    print(f"{filename}, part 2: {len(antinodes)=}")

main1("day08test1.txt")
main2("day08test1.txt")
main1("day08input.txt")
main2("day08input.txt")
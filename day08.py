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

def find_nodes(grid : np.ndarray):
    node_labels = [x for x in np.unique(grid) if x != '.']
    nodes       = dict()
    node_points = set()
    for label in node_labels:
        nodes[label] = {(i,j) for i,j in np.argwhere(grid == label)}
        node_points.update(nodes[label])
    return nodes, node_points

def find_antinodes(grid : np.ndarray, node_dictionary : dict, depth : int):
    HEIGHT = grid.shape[0]
    WIDTH  = grid.shape[1]
    all_antinodes  = set()
    for node in node_dictionary:
        positions = set(node_dictionary[node])
        for pos1 in positions:
            p1 = np.array(pos1)
            for pos2 in positions.difference({pos1}):
                p2 = np.array(pos2)
                delta = p2 - p1
                for n in range(1, depth+1):
                    all_antinodes.add(tuple(p1 - n*delta))
                    all_antinodes.add(tuple(p2 + n*delta))
    # filter out all the antinodes that are out-of-bounds
    return {(i,j) for i,j in all_antinodes if 0 <= i < HEIGHT and 0 <= j < WIDTH}

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
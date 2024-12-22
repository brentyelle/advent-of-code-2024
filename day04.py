import numpy as np

def process_file(filename : str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
    return lines

def find_horizontal(grid : np.ndarray) -> int:
    horiz_strings = ["".join(row) for row in grid]
    xmas_count = 0
    for line in horiz_strings:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")
    return xmas_count

def find_vertical(grid : np.ndarray) -> int:
    vert_strings = ["".join(row) for row in grid.T]
    xmas_count = 0
    for line in vert_strings:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")
    return xmas_count

def find_diagonals(grid : np.ndarray) -> int:
    WIDTH  = len(grid[0])
    HEIGHT = len(grid)
    gridFlip = np.fliplr(grid)
    diag_strings = []
    for k in range(-HEIGHT+1, WIDTH):
        # diagonals going down to the right
        diag_strings.append("".join(list(np.diag(grid,     k))))
        # diagonals going down to the left
        diag_strings.append("".join(list(np.diag(gridFlip, k))))
    
    xmas_count = 0
    for line in diag_strings:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")
    return xmas_count

def find_x_of_MAS(grid: np.ndarray) -> int:
    WIDTH  = len(grid[0])
    HEIGHT = len(grid)
    # every X of MAS has an A at its center
    coords_of_A = [(i,j) for [i,j] in np.argwhere(grid == 'A') if i > 0 and i < HEIGHT-1 and j > 0 and j < WIDTH-1]
    # count every X-MAS in every configuration
    x_mas_count = 0
    for i,j in coords_of_A:
        # Ms on top
        if    grid[i-1][j-1] == 'M' and \
              grid[i-1][j+1] == 'M' and \
              grid[i+1][j-1] == 'S' and \
              grid[i+1][j+1] == 'S':
              x_mas_count += 1
        # Ms on bottom
        elif  grid[i-1][j-1] == 'S' and \
              grid[i-1][j+1] == 'S' and \
              grid[i+1][j-1] == 'M' and \
              grid[i+1][j+1] == 'M':
              x_mas_count += 1
        # Ms on left
        elif  grid[i-1][j-1] == 'M' and \
              grid[i-1][j+1] == 'S' and \
              grid[i+1][j-1] == 'M' and \
              grid[i+1][j+1] == 'S':
              x_mas_count += 1
        # Ms on right
        elif  grid[i-1][j-1] == 'S' and \
              grid[i-1][j+1] == 'M' and \
              grid[i+1][j-1] == 'S' and \
              grid[i+1][j+1] == 'M':
              x_mas_count += 1
    return x_mas_count


def main1(filename):
    letterGrid = np.array(process_file(filename))
    xmas_counts = find_horizontal(letterGrid) + find_vertical(letterGrid) + find_diagonals(letterGrid)
    print(f"{filename}, part 1: {xmas_counts=}")

def main2(filename):
    letterGrid = np.array(process_file(filename))
    x_mas_counts = find_x_of_MAS(letterGrid)
    print(f"{filename}, part 2: {x_mas_counts=}")

main1("day04test.txt")
main1("day04input.txt")
main2("day04test.txt")
main2("day04input.txt")
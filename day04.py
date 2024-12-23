import numpy as np

def process_file(filename : str) -> np.ndarray:
    """Reads the file as a 2D `numpy` array of characters.\n
    Trailing whitespace is trimmed before conversion."""
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
    return np.array(lines)

# ====== Part 1 Functions ======

def count_all_xmas(stringlist : list[str]) -> int:
    """Count all occurrences of `XMAS` forwards and backwards in each `str`-element of the list `stringlist`.\n
    Since `XMAS` cannot overlap itself, we needn't worry about the fact that the `.count()` method only counts non-overlapping instances."""
    xmas_count = 0
    for line in stringlist:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")
    return xmas_count

def find_horizontal_vertical(grid : np.ndarray) -> int:
    """Convert each row and column into a string, then count all occurrences of XMAS forwards and backwards in all of those strings."""
    horiz_strings = ["".join(row) for row in grid  ]
    vert_strings  = ["".join(row) for row in grid.T]
    return count_all_xmas(horiz_strings + vert_strings)

def find_diagonals(grid : np.ndarray) -> int:
    """Convert each diagonal (both ways) into a string, then count all occurrences of XMAS forwards and backwards in all of those strings."""
    WIDTH  = len(grid[0])
    HEIGHT = len(grid)
    GRID_FLIPPED = np.fliplr(grid)
    # first, get string versions of all of the diagonals
    diag_strings = []
    for k in range(-HEIGHT+1, WIDTH):
        # diagonals going down to the right
        diag_strings.append("".join(np.diag(grid,         k)))
        # diagonals going down to the left
        diag_strings.append("".join(np.diag(GRID_FLIPPED, k)))
    return count_all_xmas(diag_strings)

# ====== Part 2 Function ======

def find_x_of_MAS(grid: np.ndarray) -> int:
    """Counts the number of instances of an X of `MAS` in the given `grid`.\n
    Note that there are four configurations, named here depending on where the two `M`s are: top, bottom, left, right.
    In addition, note that all configurations necessarily have `A` in their center, so we can begin the search by looking for all `A`s--omitting those on the edge of the grid, since they don't have room for an X-`MAS`."""
    WIDTH  = len(grid[0])
    HEIGHT = len(grid)
    # find the indices all `A`s not on the edge
    coords_of_A = [(i,j) for i,j in np.argwhere(grid == 'A') if i > 0 and i < HEIGHT-1 and j > 0 and j < WIDTH-1]
    # check each found `A` to see if it's the center of an X-`MAS`
    x_mas_count = 0
    for i,j in coords_of_A:
        four_corners = str(  grid[i-1][j-1]     # above-left
                           + grid[i-1][j+1]     # above-right
                           + grid[i+1][j-1]     # below-left
                           + grid[i+1][j+1])    # below-right
        if (   four_corners == "MMSS"           # MM above
            or four_corners == "SSMM"           # MM below
            or four_corners == "MSMS"           # MM on left
            or four_corners == "SMSM"):         # MM on right
            x_mas_count += 1
    return x_mas_count

# ====== Main Functions ======

def main1(filename):
    letterGrid = process_file(filename)
    xmas_counts = find_horizontal_vertical(letterGrid) + find_diagonals(letterGrid)
    print(f"{filename}, part 1: {xmas_counts=}")

def main2(filename):
    letterGrid = process_file(filename)
    x_mas_counts = find_x_of_MAS(letterGrid)
    print(f"{filename}, part 2: {x_mas_counts=}")

main1("day04test.txt")
main2("day04test.txt")
main1("day04input.txt")
main2("day04input.txt")
import numpy as np
from enum import Enum
import cProfile

OBSTACLE_CHAR = '#'
STARTING_CHAR = '^'

class Direction(Enum):
    """The underlying numbers were chosen such that movement could be calculated branchlessly."""
    NORTH   = 0
    SOUTH   = 1
    EAST    = 2
    WEST    = 3

def turn_right(dir: Direction) -> Direction:
    """Given a `Direction`, returns the `Direction` pointing 90° to the right (i.e., clockwise)."""
    match (dir):
        case Direction.NORTH:
            return Direction.EAST
        case Direction.EAST:
            return Direction.SOUTH
        case Direction.SOUTH:
            return Direction.WEST
        case Direction.WEST:
            return Direction.NORTH
        case _:
            raise ValueError(f"{dir=} is not a valid direction enum")

def process_file(filename : str) -> np.ndarray:
    """Reads the file as a 2D `numpy` array of characters.\n
    Trailing whitespace is trimmed before conversion."""
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
    return np.array(lines)

def follow_route(lab_map : np.ndarray) -> tuple[np.ndarray, bool]:
    """Given a laboratory grid `lab_map` with:
    * a guard's starting position marked by `^`
    * obstacles marked by `#`\n
    Follows the path until the guard either goes out-of-bounds or follows an infinite loop."""
    visit_counts    = np.zeros(shape=(lab_map.shape[0], lab_map.shape[1], 5), dtype=int)
    obstacles       = tuple((i,j) for i,j in np.argwhere(lab_map == OBSTACLE_CHAR))
    current_pos     = tuple(np.argwhere(lab_map == STARTING_CHAR)[0])
    current_dir     = Direction.NORTH   # guard always begins northward
    MAX_HEIGHT      = lab_map.shape[0]
    MAX_WIDTH       = lab_map.shape[1]
    is_stuck_in_loop= False

    # until we go out of bounds or start looping
    while 0 <= current_pos[0] < MAX_HEIGHT and 0 <= current_pos[1] < MAX_WIDTH:
        # position_triplet consists of current position and current direction
        position_triplet = (current_pos[0], current_pos[1], current_dir.value)
        visit_counts[position_triplet] += 1
        # if we ever re-visit a position from the same direction, we're going in an infinite loop
        if visit_counts[position_triplet] > 1:
            is_stuck_in_loop = True
            break
        # calculate where we're currently trying to go
        """Turns out that this "smart" method was actually less efficient!"""
        # NS_adjustment = current_dir.value%2 * current_dir.value
        # EW_adjustment = abs(current_dir.value)//2 * np.sign(current_dir.value)
        # next_pos_attempt = (current_pos[0] + NS_adjustment, current_pos[1] + EW_adjustment)
        """And this method with a `match` statement was faster!"""
        match current_dir:
            case Direction.NORTH:
                next_pos_attempt = (current_pos[0] - 1, current_pos[1]    )
            case Direction.EAST:
                next_pos_attempt = (current_pos[0]    , current_pos[1] + 1)
            case Direction.SOUTH:
                next_pos_attempt = (current_pos[0] + 1, current_pos[1]    )
            case Direction.WEST:
                next_pos_attempt = (current_pos[0]    , current_pos[1] - 1)
            case _:
                raise ValueError(f"{current_dir=} is not a valid direction enum")
        # if it's blocked, turn right instead of moving
        if next_pos_attempt in obstacles:
            current_dir = turn_right(current_dir)
        # if it's not blocked, actually move there
        else:
            current_pos = next_pos_attempt

    visited_list = [(i,j) for i,j in np.argwhere(np.sum(visit_counts, axis=2) > 0)]
    return visited_list, is_stuck_in_loop

def main1(filename : str):
    """Counts the number of tiles that the guard visits in the laboratory, including the starting position."""
    laboratory_map  = process_file(filename)
    visited_list, _ = follow_route(laboratory_map)
    print(f"{filename}, part 1: {len(visited_list)=}")

def main2(filename : str):
    """Counts the number of places where an obstacle could be placed to make the guard go in an infinite loop.\n
    Regrettably, the current method is quite inefficient, requiring about 10~20 minutes to solve."""
    laboratory_map  = process_file(filename)
    STARTING_POS    = tuple(np.argwhere(laboratory_map == STARTING_CHAR)[0])
    visited_list, _ = follow_route(laboratory_map)
    visited_list = [(i,j) for i,j in visited_list if (i,j) != STARTING_POS]
    infinite_loop_count = 0
    position_counter = 0
    for i,j in visited_list:
        position_counter += 1
        if position_counter % 300 == 0:
            print(f"trying position {position_counter} of {len(visited_list)}, found {infinite_loop_count} infinite loops so far")
            break
        laboratory_map_plus_one = laboratory_map.copy()
        laboratory_map_plus_one[i,j] = OBSTACLE_CHAR
        _, did_loop = follow_route(laboratory_map_plus_one)
        infinite_loop_count += int(did_loop)
    print(f"{filename}, part 2: {infinite_loop_count=} ways to add obstacles to infinite-loop")

main1("day06test.txt")
main2("day06test.txt")
main1("day06input.txt")
main2("day06input.txt")

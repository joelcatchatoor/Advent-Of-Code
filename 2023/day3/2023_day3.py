from typing import List, Tuple, Set
import time

# Constants for the script
INPUT_FILE = "day3_input.txt"
OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def parse(input_file: str) -> List[List[str]]:
    """
    Parses the engine schematic from an input file into a 2D list.

    Args:
        input_file (str): The path to the file containing the engine schematic.

    Returns:
        List[List[str]]: A 2D list representing the engine schematic, where each inner list is a row of the schematic.
    """
    with open(input_file) as file:
        grid = file.read().splitlines()
        
        for idx, line in enumerate(grid):
            grid[idx] = list(line)
        
        return grid

def find_number(y: int, x: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Finds and returns the number at a specified location in the grid and its coordinates.

    Args:
        y (int): The y-coordinate (row index) in the grid.
        x (int): The x-coordinate (column index) in the grid.
        grid (List[List[str]]): The engine schematic grid.
        visited (Set[Tuple[int, int]]): A set of visited coordinates.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: A tuple containing the number found (if any) and a list of its coordinates.
    """
    if (y, x) in visited or not grid[y][x].isdigit():
        return 0, []

    digits = []
    coords = []

    # Check to the left
    i = 0
    while x - i >= 0 and grid[y][x - i].isdigit():
        visited.add((y, x - i))
        digits.insert(0, grid[y][x - i])  # Insert at the beginning
        coords.insert(0, (y, x - i))
        i += 1

    # Check to the right (excluding the starting point)
    i = 1
    while x + i < len(grid[0]) and grid[y][x + i].isdigit():
        visited.add((y, x + i))
        digits.append(grid[y][x + i])
        coords.append((y, x + i))
        i += 1

    return int(''.join(digits)), coords

def is_adjacent_to_symbol(y: int, x: int, grid: List[List[str]]) -> bool:
    """
    Checks if a given position in the grid is adjacent to any symbol.

    Args:
        y (int): The y-coordinate (row index) in the grid.
        x (int): The x-coordinate (column index) in the grid.
        grid (List[List[str]]): The engine schematic grid.

    Returns:
        bool: True if adjacent to a symbol, False otherwise.
    """
    for offset_y, offset_x in OFFSETS:
        ny, nx = y + offset_y, x + offset_x

        if (0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and not 
            grid[ny][nx].isdigit() and not grid[ny][nx] == "."): 
            return True
        
    return False

def solve_part1(grid: List[List[str]]) -> int:
    """
    Solves Part 1 of the challenge by summing up all part numbers in the grid.

    Args:
        grid (List[List[str]]): The engine schematic grid.

    Returns:
        int: The sum of all part numbers.
    """
    total = 0
    visited = set()

    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            number, coords = find_number(y, x, grid, visited)
            if number and any(is_adjacent_to_symbol(coord_y, coord_x, grid) for coord_y, coord_x in coords):
                total += number
    
    return total

def is_adjacent_to_numbers(y: int, x: int, grid: List[List[str]]) -> int:
    """
    Calculates the product of two part numbers adjacent to a gear symbol.

    Args:
        y (int): The y-coordinate (row index) of the gear symbol.
        x (int): The x-coordinate (column index) of the gear symbol.
        grid (List[List[str]]): The engine schematic grid.

    Returns:
        int: The product of two adjacent part numbers or 0 if not a valid gear.
    """
    visited_adjacent = set()
    numbers = []
    
    for offset_y, offset_x in OFFSETS:
        ny, nx = y + offset_y, x + offset_x

        if(0 <= ny < len(grid) and 0 <= nx < len(grid[0])):

            number, _ = find_number(ny, nx, grid, visited_adjacent)

            if number:
                numbers.append(number)

    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    else:
        return 0

def solve_part2(grid: List[List[str]]) -> int:
    """
    Solves Part 2 of the challenge by calculating the sum of all gear ratios in the grid.

    Args:
        grid (List[List[str]]): The engine schematic grid.

    Returns:
        int: The sum of all gear ratios.
    """
    total = 0
    visited = set()

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "*" and not (y, x) in visited:
                
                visited.add((y, x))
                total += is_adjacent_to_numbers(y, x, grid)
    
    return total

def main() -> None:
    """
    Main function to execute the script.

    Parses the input file, solves both parts of the challenge, and prints the answers along with the execution time.
    """
    tic = time.perf_counter()
    
    data = parse(INPUT_FILE)

    part1_answer = solve_part1(data)  
    part2_answer = solve_part2(data)

    print("The answer to part 1 is " + str(part1_answer))
    print("The answer to part 2 is " + str(part2_answer))

    
    toc = time.perf_counter()
    
    print(f"Completed in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()

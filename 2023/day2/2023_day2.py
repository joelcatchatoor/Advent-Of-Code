import re
from typing import List
import time

# Constants for the script
INPUT_FILE = "day2_input.txt"
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

def parse(input_file: str) -> List[str]:
    """
    Parses the input file and returns a list of lines.

    Args:
        input_file (str): The path to the input file.

    Returns:
        List[str]: A list of strings, each representing a line from the input file.
    """
    with open(input_file) as file:
        return file.read().splitlines()

def process_line_part1(line: str) -> int:
    """
    Processes a line of the input for part 1 of the challenge.
    
    It determines if the game represented by the line is possible with the given MAX_CUBES constraints.
    
    Args:
        line (str): A string representing a single line from the input file.
        
    Returns:
        int: The game ID if the game is possible, otherwise 0.
    """
    split_line = line.split(": ", 1)

    game_id = int(re.search("\d+", split_line[0]).group())

    turns = split_line[1].split("; ")

    for turn in turns:
        reveals = turn.split(", ")

        for reveal in reveals:
            colour = re.search("[a-z]+", reveal).group()
            count = int(re.search("\d+", reveal).group())

            if count > MAX_CUBES[colour]:
                return 0
            
    return game_id

def solve_part1(lines: List[str]) -> int:
    """
    Solves part 1 of the challenge.

    It computes the sum of the IDs of the games that are possible under the MAX_CUBES constraints.

    Args:
        lines (List[str]): A list of strings representing the input lines.

    Returns:
        int: The sum of the IDs of the games that are possible.
    """
    total = 0
    for line in lines:
        total += process_line_part1(line)

    return total

def process_line_part2(line: str) -> int:
    """
    Processes a line of the input for part 2 of the challenge.
    
    It calculates the 'power' of the minimum set of cubes required for the game represented by the line.
    
    Args:
        line (str): A string representing a single line from the input file.
        
    Returns:
        int: The 'power' of the minimum set of cubes required for the game.
    """
    mins_dict = {'red': 0, 'blue': 0, 'green': 0}

    split_line = line.split(": ", 1)

    turns = split_line[1].split("; ")

    for turn in turns:
        reveals = turn.split(", ")

        for reveal in reveals:
            colour = re.search("[a-z]+", reveal).group()
            count = int(re.search("\d+", reveal).group())

            if count > mins_dict[colour]:
                mins_dict[colour] = count

    return mins_dict["red"] * mins_dict["blue"] * mins_dict["green"]  

def solve_part2(lines: List[str]) -> int:
    """
    Solves part 2 of the challenge.

    It computes the sum of the 'power' of the minimum sets of cubes required for each game.

    Args:
        lines (List[str]): A list of strings representing the input lines.

    Returns:
        int: The sum of the 'power' of the minimum sets of cubes for all games.
    """
    total = 0
    for line in lines:
        total += process_line_part2(line)

    return total

def main() -> None:
    """
    Main function to execute the script.

    It parses the input file, solves both parts of the challenge, and prints the answers along with the execution time.
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
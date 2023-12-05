import time
import re
from typing import List

# Constants for the script
PART2 = True
INPUT_FILE = 'day1_input.txt'

# Mapping of words to their corresponding digit
MAPPING = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Regular expression pattern for Part 1: Find any digit
PATTERN_PART1 = r"\d"

# Regular expression patterns for Part 2: Find any digit or spelled-out digit
PATTERN_PART2_A = r"(one|two|three|four|five|six|seven|eight|nine|\d)"
PATTERN_PART2_B = r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)"

def parse(input_file: str) -> List[str]:
    """
    Parses the given input file and returns a list of lines.

    Args:
    - input_file (str): The path to the input file.

    Returns:
    - List[str]: A list of strings, each representing a line from the input file.
    """
    with open(input_file) as file:
        return file.read().splitlines()

def convert_word_to_digit(word: str) -> str:
    """
    Converts a word representing a number to its corresponding digit string.

    Args:
    - word (str): The word to be converted.

    Returns:
    - str: The corresponding digit string.
    """
    return MAPPING.get(word)

def process_line(line: str) -> int:
    """
    Processes a single line to find and combine the first and last digits.

    Args:
    - line (str): The line to process.

    Returns:
    - int: The combined two-digit number.
    """
    if PART2:
        first_match = re.search(PATTERN_PART2_A, line)
        last_match = re.search(PATTERN_PART2_B, line[::-1])
    else:
        first_match = re.search(PATTERN_PART1, line)
        last_match = re.search(PATTERN_PART1, line[::-1])

    if first_match.group().isdigit():
        first_digit = first_match.group()
    else:
        first_digit = convert_word_to_digit(first_match.group())

    if last_match.group().isdigit():
        second_digit = last_match.group()
    else:
        second_digit = convert_word_to_digit(last_match.group()[::-1])

    return int(first_digit + second_digit)

def solve(parsed_input: List[str]) -> int:
    """
    Solves the calibration value challenge by processing each line.

    Args:
    - parsed_input (List[str]): The parsed input lines.

    Returns:
    - int: The sum of all calibration values.
    """
    total = 0
    for line in parsed_input:
        total += process_line(line)
    
    return total

def main() -> None:
    """
    Main function to execute the script.
    It calculates and prints the total calibration value and execution time.
    """
    tic = time.perf_counter()
    
    answer = solve(parse(INPUT_FILE))    
    print(answer)
    
    toc = time.perf_counter()
    
    print(f"Completed in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
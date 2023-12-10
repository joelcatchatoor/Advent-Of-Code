from typing import List, Tuple, Set
import time
import re
from queue import Queue

# Constants for the script
INPUT_FILE = "day4_input.txt"

def parse(input_file: str) -> List[Tuple[int, Set[int], Set[int]]]:
    """
    Parses the input file and extracts the information about each scratchcard.

    Args:
    input_file (str): The path to the file containing the scratchcards data.

    Returns:
    List[Tuple[int, Set[int], Set[int]]]: A list of tuples, each representing a scratchcard. 
    Each tuple contains the card ID (int), a set of winning numbers (Set[int]), 
    and a set of the user's numbers (Set[int]).
    """
    with open(input_file) as file:
        cards = file.read().splitlines()

        parsed_cards = []
        for card in cards:
            
            card = re.sub(r"Card\s+", "", card)
            card_id, numbers = re.split(r":\s+", card)
            winning_numbers, your_numbers = numbers.split(" | ")

            card_id_int = int(card_id) - 1 # adjust for 0-based indexing

            winning_numbers_set = {int(num) for num in winning_numbers.split()}
            your_numbers_set = {int(num) for num in your_numbers.split()}

            parsed_cards.append((card_id_int, winning_numbers_set, your_numbers_set))

        return parsed_cards

def calc_card_points(card: Tuple[int, Set[int], Set[int]]) -> int:
    """
    Calculates the points for a given scratchcard based on the number of matching numbers.

    Args:
    card (Tuple[int, Set[int], Set[int]]): A tuple representing a scratchcard, 
    containing the card ID, set of winning numbers, and set of user's numbers.

    Returns:
    int: The calculated points for the card.
    """
    matching_numbers_set = card[1].intersection(card[2])

    if matching_numbers_set:
        return 2 ** (len(matching_numbers_set) - 1)
    else:
        return 0

def solve_part1(cards: List[Tuple[int, Set[int], Set[int]]]) -> int:
    """
    Solves Part 1 of the challenge by calculating the total points of all scratchcards.

    Args:
    cards (List[Tuple[int, Set[int], Set[int]]]): The list of scratchcards.

    Returns:
    int: The total points of all scratchcards.
    """
    total = 0
    
    for card in cards:
        total += calc_card_points(card)

    return total

def solve_part2(cards: List[Tuple[int, Set[int], Set[int]]]) -> int:
    """
    Solves Part 2 of the challenge by calculating the total number of scratchcards 
    including the originals and all additional winnings.

    Args:
    cards (List[Tuple[int, Set[int], Set[int]]]): The list of scratchcards.

    Returns:
    int: The total number of scratchcards after processing all winnings.
    """
    q = Queue()

    for card in cards:
        q.put(card)

    total_cards = len(cards)

    while not q.empty():
        card = q.get()
        matches = len(card[1].intersection(card[2]))

        for i in range(matches):
            next_card_index = card[0] + i + 1

            if next_card_index < len(cards):
                q.put(cards[next_card_index])
                total_cards += 1

    return total_cards

def main() -> None:
    """
    Main function to execute the script. It parses the input file, 
    solves both parts of the challenge, and prints the answers along with the execution time.
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
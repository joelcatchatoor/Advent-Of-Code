import numpy as np

def parse(input_file):
    """Parse input to 1D NumPy array and a 3D NumPy array from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    # the series of drawn numbers appear first in the text file input. They are separated by two line breaks from the boards.
    # stores element [0] from a split by two line breaks
    drawn_nums_str = contents.split("\n\n")[0]
    # splits the string by comma, then converts individiual elements to integers
    # drawn_nums is a list of integers
    drawn_nums = [int(x) for x in drawn_nums_str.split(",")]
    
    # stores all elements from [1] onwards, split by two line breaks. This captures all boards. 
    # list of strings, each board is saved one string each
    boards_str = contents.split("\n\n")[1:]
    # each board becomes a list, each row becomes a string.
    boards_list_of_lists = [x.split("\n") for x in boards_str]
    # each row becomes a list of strings of individual numbers
    # this is now a list of boards, each with lists of rows, each with lists of numbers.
    boards_lists_3 = [[x.split() for x in row] for row in boards_list_of_lists]
    # each number becomes an integer from a string.
    boards_lists_3_ints = [[[int(x) for x in row] for row in board] for board in boards_lists_3]

    # returns a tuple of two NumPy arrays: the drawn numbers and the boards to play
    return (np.array(drawn_nums), np.array(boards_lists_3_ints))

def find_winning_board(drawn_nums, boards, draw_count):
    """Simulates a game of bingo (where the sequence of drawn numbers is known at the start).
     Checks an increasing number of drawn numbers against every board by matching numbers in each board to the drawn numbers, 
     then checking to see if this makes a full row or column match, thus winning the game."""

    while draw_count <= len(drawn_nums):
   
        for board in boards:
                
                matches = np.isin(board, drawn_nums[:draw_count])
                
                for row in matches:
                    if row.all() == True:
                        # sum all the numbers marked False in matches
                        # return the winning board, the matches (bool array), and the draw count
                        return (board, matches, draw_count)

                    else:
                        for transposed_row in matches.transpose():
                            if transposed_row.all() == True:
                                # sum all the numbers marked False in matches
                                # return the winning board, the matches (bool array), and the draw count
                                return (board, matches, draw_count)
        
        draw_count += 1

def solve_part1(nums_and_boards):
    """Function to solve puzzle part 1.
    Finds the first winning board then multiples the sum of the unmarked numbers (False) by the final number that was drawn to win the game.
    Takes tuple containing a 1D NumPy array and a 3D NumPy array as input."""

    # separates out the input tuple for readibility
    drawn_nums = nums_and_boards[0]
    boards = nums_and_boards[1]
    # starts from the first five numbers (positions 0 to 4), since this is the first time a full row or column could be achieved.
    draw_count = 5

    # finds the first winning board
    # winning_board equals a tuple with three elements: board, matches, draw_count.
    winning_board = find_winning_board(drawn_nums, boards, draw_count)

    # NOTES:
    # sum of unmarked numbers (winning_board[1] is matches, select those equal to False from the board that won)
    # drawn_nums[this needs to be zero-indexed], hence [winning_board[2] (which is draw_count) minus one.
    return sum(winning_board[0][winning_board[1] == False]) * drawn_nums[winning_board[2]-1]

def solve_part2(nums_and_boards):
    """Solves puzzle part 2.
    Finds the last winning board then then multiples the sum of the unmarked numbers (False) by the final number that was drawn to win the game.
    It exhausts the number of winning boards (winning_board is None), then re-runs the final game which had a winning board.
    Every time a winning board is successfully found, that board is removed from the boards used in the next game.
    Takes tuple containing a 1D NumPy array and a 3D NumPy array as input."""

    drawn_nums = nums_and_boards[0]
    boards = nums_and_boards[1]
    # starts from the first five numbers (positions 0 to 4), since this is the first time a full row or column could be achieved.
    draw_count = 5

    # loops until no winning board is found
    while True:
        # runs a game of bingo to find a winning board
        winning_board = find_winning_board(drawn_nums, boards, draw_count)

        # eventually, the drawn nums will be exhausted without a winner, and so returning None
        if winning_board is None:
            # re-runs the previous game of bingo, reintroducing the final winning board that would have been deleted in the previous loop iteration
            winning_board = find_winning_board(drawn_nums, previous_boards, draw_count)
            # returns the product of the sum of the unmarked numbers with the final number that was drawn
            return sum(winning_board[0][winning_board[1] == False]) * drawn_nums[winning_board[2]-1]

        else:
            # find the index of the winning board
            winning_board_index = np.where(np.all(winning_board[0] == boards, axis=(1,2)))[0][0]

            # save the current array of boards, including the board that has just won
            previous_boards = boards
            # remove the board that has just won from the main boards array
            boards = np.delete(boards, winning_board_index, axis=0)


def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day4_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
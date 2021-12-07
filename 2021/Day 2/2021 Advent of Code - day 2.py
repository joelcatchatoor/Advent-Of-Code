def parse(input_file):
    """Parse input to list of lists (containing a string and an integer each: 'direction' and amount) from file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()

    def refine_output(x):
        """splits line to a list of two strings, then converts the second string to an integer"""
        list_x = x.split()
        list_x[1] = int(list_x[1])
        return list_x        
    
    # splits contents to a list of lines (strings), then returns a list of lists
    # example output [['forward', 4],['up', 2]]
    return [refine_output(x) for x in contents.splitlines()] 
    
def solve_part1(movements):
    """Solution to part 1. 
    Returns the product of: sum forward movement and sum depth (down and up) movement.
    Takes a list of lists of strings as input"""
    
    # create three separate lists of integer movement amounts in the different directions
    forwards = [x[1] for x in movements if x[0] == 'forward']
    ups = [x[1] for x in movements if x[0] == 'up']
    downs = [x[1] for x in movements if x[0] == 'down']

    # sum the integer movements
    sum_forward = sum(forwards)
    sum_depth = sum(downs) - sum(ups)

    # return the product of these sums
    return sum_forward * sum_depth

def solve_part2(movements):
    """Solution to part 2.
    Returns the product of: sum forward movement and sum depth (aim * forward amount) movement.
    Takes a list of lists of strings as input"""

    sum_forward = 0
    sum_depth = 0
    aim = 0

    for movement in movements:
        if movement[0] == 'forward':
            sum_forward += movement[1]
            sum_depth += aim * movement[1]
        elif movement[0] == 'down':
            aim += movement[1]
        else:
            aim -= movement[1]

    return sum_forward * sum_depth

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    input_file = 'day2_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
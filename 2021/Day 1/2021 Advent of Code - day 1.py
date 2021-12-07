def parse(input_file):
    """Parse input to list of integers from file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()

    # convert contents to list of strings (splitlines), then to list of integers
    return [int(x) for x in contents.splitlines()]
    
def solve_part1(depths):
    """Solution to part 1. 
    Returns the count of depth increases from n-1 to n.
    Takes a list of integers as input"""
    # create counter
    count = 0

    # loop through depths list, comparing n-1 to n to count the number of depth increases 
    for index, depth in enumerate(depths):
        # start the comparison from the second position (1) in the list
        if index > 0:
            # see if n is greater than n-1
            if depths[index] > depths[index - 1]:
                count += 1
    
    return count

def solve_part2(depths):
    """Solution to part 2. 
    Returns the count of depth increases between two three-measurement windows.
    Takes a list of integers as input"""
    count = 0

    for index, depth in enumerate(depths):
        # start the comparison from the fourth position (3) in the list
        if index > 2:
            # sum the two three-measurement sliding windows
            sum1 = depths[index-1] + depths[index-2] + depths[index-3]
            sum2 = depths[index] + depths[index-1] + depths[index-2]

            # see if the second three-measurement window is greater than the first.
            if sum2 > sum1:
                count += 1
    
    return count

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    input_file = 'day1_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
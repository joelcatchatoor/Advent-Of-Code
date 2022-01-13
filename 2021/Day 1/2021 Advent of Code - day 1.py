def parse(input_file):
    """Parse input to list of integers from file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()

    # convert contents to list of strings (splitlines), then to list of integers
    return [int(x) for x in contents.splitlines()]

def compare(depths, gap):
    """Returns a count of depth increases in depths from (n - gap) to n."""
    count = 0

    for index in range(gap, len(depths)):
        if depths[index] > depths[index - gap]:
            count += 1
    
    return count

def solve(input_file):
    """Solve the two-part puzzle for the input provided."""
    data = parse(input_file)

    """part 2 note: depths[index-1] and depths[index-2] occur in both three-measurement sliding windows, 
    so only need to compare depths[index] with depths[index - 3]."""
    return compare(data, 1), compare(data, 3)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    input_file = 'day1_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))

import random

def parse(input_file):
    """Parse input to list of integers from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()   

        list_str = contents.split(",")    

        return [int(x) for x in list_str]

def quickselect(positions, k):
    """Performs quickselect algorithm (random choice pivot selection) on unsorted list.
    Select the kth element in positions (list). Recursive algorithm. Accessed December 2021: https://rcoh.me/posts/linear-time-median-finding/"""

    # if only one value left, return it
    if len(positions) == 1:
        return positions[0]
    
    # the value by which all elements in list is compared (higher or lower or equal)
    pivot = random.choice(positions)

    # sub-lists of values from positions list that are lower, higher or equal to the randomly selected pivot value
    lows = [position for position in positions if position < pivot]
    highs = [position for position in positions if position > pivot]
    pivots = [position for position in positions if position == pivot]

    # if there are more lows (more numbers lower than the pivot value) than the target kth element
    if k < len(lows):
        # recursively call this algorithm, keeping the existing value of k and only using the sub-list lows 
        return quickselect(lows, k)
    
    # alternatively, if the lengths of lows and pivots are greater than k (but the length of lows by themselves are not greater than k - the first if above)
    # therefore pivots contains the kth value. since pivots contains n of the same value x (pivot), returns pivots[0]
    elif k < len(lows) + len(pivots):
        return pivots[0]
    
    # lastly, k must be greater than the length of lows and pivots
    # resursively call this algorithm, keeping only the highs, and adjusting kth element by subtracting the lengths of lows and pivots
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def find_median(positions):
    """Selects the median from an unsorted list."""
    
    # if odd number of elements in list
    if len(positions) % 2 == 1:
        # k = integer division of length by 2.  e.g. 11 // 2 = 5 (6th position of a zero indexed list) 
        return int(quickselect(positions, len(positions) // 2))
    # if even number of elements in list
    else:        
        # return the average of the the middle two numbers 
        return int((quickselect(positions, (len(positions) / 2)) + quickselect(positions, (len(positions) / 2) - 1)) / 2)

def calc_fuel_constant(positions, alignment_point):
    """sums the distance between each number in the unsorted list and the median value"""
    fuel = 0

    for position in positions:
        fuel += abs(position - alignment_point)

    return fuel

def calc_fuel_increasing(positions, alignment_point):
    """finds the total fuel needed where, for each crab submarine (lol), each change of 1 step costs 1 more unit of fuel than the last"""

    fuel = 0

    for position in positions:
        distance = abs(position - alignment_point)

        i = 1

        while i <= distance:
            fuel += i
            i += 1
    
    return fuel

def solve_part1(positions):
    """Solves puzzle part 1.
    My starting theory was that aligning on the median would consistently deliver the cheapest outcome. 
    (the example alignment point is 2, which is the median)."""

# quickselect the median
    median = find_median(positions)
    
# find 'fuel' required to get all numbers to the median
    return calc_fuel_constant(positions, median)

def solve_part2(positions):
    """Solves puzzle part 2.
    Aligns on the mean average this time, with some rounding. 
    (Example data the mean is 4.9, the example optimal alignment point is 5)"""

    # calc the mean average of positions and round to nearest integer
    mean = round(sum(positions) / len(positions))

    # calc either side of the rounded mean
    result1 = calc_fuel_increasing(positions, mean + 1)
    result2 = calc_fuel_increasing(positions, mean)
    result3 = calc_fuel_increasing(positions, mean - 1)

    # check to determine the cheapest outcome 
    if result1 < result2 and result1 < result3:
        return result1
    elif result2 < result1 and result2 < result3:
        return result2
    else:
        return result3

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day7_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
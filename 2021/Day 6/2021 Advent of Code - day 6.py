"""Python 3.6+ required to ensure a dictionary is insertion ordered."""

def parse(input_file):
    """Parse input to list of strings ['1', '2', '0'] from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    # split input string to a list of strings. separate by comma
    return contents.split(",")
    
def lanternfish_growth(fish_timer_list, days):
    """Solves puzzle part 1 & 2. Counts and then models the number of fish at each day of the 8-day cycle, over x days.
    This approach is faster and more efficient than working with the values for invididual fish in a huge array."""

    # dictionary to store the count of fish at each day of the cycle as integers
    timer_cycle_count = { '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0 }

    # add the counts of input (starter) values to the dictionary
    for key in timer_cycle_count:
        # .count(key) is possible because of the names of the dictionary keys are the same as the values in fish_timer_list to be counted.
        timer_cycle_count[key] = fish_timer_list.count(key)

    i = 0
    
    while i < days:
        # stores value of the number of fish that are on day 0 of the cycle
        new_fish = timer_cycle_count['0']

        # this requires Python 3.6+ as it must loop in insertion order ('0' to '8')
        for key in timer_cycle_count:
            # assigns fish coming down from day 7 plus existing fish resetting to day 6 from day 0 (new_fish)
            if key == '6':
                timer_cycle_count[key] = timer_cycle_count[str(int(key) + 1)] + new_fish
            # assigns new_fish as these are the ones who start at day 8
            elif key == '8':
                timer_cycle_count[key] = new_fish
            # assigns fish coming down from str(int(key) + 1)) i.e. day '3' is assigned what was day '4' i.e. str(3 + 1)
            else:
                timer_cycle_count[key] = timer_cycle_count[str(int(key) + 1)]

        i += 1

    # sums the values of the whole dictionary to find the total number of fish
    return sum(timer_cycle_count.values())

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    # part 1 is 80 days, part 2 is 256 days. Same function.
    return lanternfish_growth(data, 80), lanternfish_growth(data, 256)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day6_exampleinput.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
def parse(input_file):
    """Parse input to list of lists from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    lines = contents.splitlines()
    # each inner list is firstly the ten unique signal patterns and secondly the four digit (represented as string patterns) output value
    return [x.split(" | ") for x in lines]

def solve_part1(data):
    """Solves puzzle part 1."""

    # just need the four output values
    outputs = [x[1] for x in data]
    # convert to list of lists (inner list the four string patterns that represent the four digit output values)
    outputs_split = [x.split() for x in outputs]

    # ready to count strings of different lengths
    ones = 0
    sevens = 0
    fours = 0
    eights = 0

    # count of strings of relevant lengths
    for row in outputs_split:
        for num in row:
            length = len(num)

            # one is the only number to have just two letters in the string pattern, etc. 
            if length == 2:
                ones += 1
            elif length == 3:
                sevens += 1
            elif length == 4:
                fours += 1
            elif length == 7:
                eights += 1
            
    # sum the counts of strings of different lengths
    return ones + sevens + fours + eights

def solve_part2(data):
    """Solves puzzle part 2."""

    # split out and save the ten unique signal patterns (inputs) and the string patterns of the four digit output values (outputs)
    inputs = [x[0] for x in data]
    inputs_split = [x.split() for x in inputs]
    outputs = [x[1] for x in data]
    outputs_split = [x.split() for x in outputs]

    # this will store the four digit output values (as integers)
    values = []
    
    # loop through every row in inputs(split) to find the four digit output value for each and append it to values list
    for index, row in enumerate(inputs_split):
        
        # create empty dictionary to store string patterns once they are correctly deduced.
        digits = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
        
        # find '0', '7', '4' and '8'
        for num in row:
            length = len(num)

            # one is the only number to have just two letters in the string pattern, etc. 
            if length == 2:
                digits['1'] = num
            elif length == 3:
                digits['7'] = num
            elif length == 4:
                digits['4'] = num
            elif length == 7:
                digits['8'] = num

        # split the string patterns for '4' and '7' each into a list of characters
        char_seven = [char for char in digits['7']]
        char_four = [char for char in digits['4']]

        # create sub-lists of string patterns that are 5 and 6 characters long
        length_five = [str for str in row if len(str) == 5]
        length_six = [str for str in row if len(str) == 6]
        
        # find '3' - length of 5 and matches all three characters in digits['7'] (in other words, the segments comprising 7 are all in 3. This is unique among the digits that use five segments (are 5 long))
        for num in length_five:
            match_list = [char in char_seven for char in num]
            # count there are three Trues
            if sum(match_list) == 3:
                digits['3'] = num
                # remove the string pattern for 3 to make the following deductions easier
                length_five.remove(num)

        # find '9' - length of 6 and matches all four characters in digits['4'] (in other words, the segments comprising 4 are all in 6. this is unique among the digits that use six segments).
        for num in length_six:
            match_list = [char in char_four for char in num]

            if sum(match_list) == 4:
                digits['9'] = num
                # remove the string pattern for 9 to make the following deductions easier
                length_six.remove(num)

        # find '5' and '6' - '6' is length of six (six segments) and matches all five characters in the string pattern that then needs to be assigned to '5'
        for num_five in length_five:
            char_list = [char for char in num_five]
                
            for num_six in length_six:
                match_list = [char in char_list for char in num_six]

                if sum(match_list) == 5:
                    digits['6'] = num_six
                    digits['5'] = num_five
                    length_six.remove(num_six)
                    length_five.remove(num_five)
        
        # assign '2' and '0' from being the only remaining vales in length_five and length_six respectively
            digits['2'] = length_five[0]
            digits['0'] = length_six[0]
        
        # match to the four digits of the output value:
        value = []
        
        # decode the four digit output value for this row (using index from the outer loop)
        for digit in outputs_split[index]:
            length = len(digit)
            char_list = [char for char in digit]
            
            if length == 2:
                value.append(1)
            elif length == 3:
                value.append(7)
            elif length == 4:
                value.append(4)
            elif length == 5:
                match_two = [char in char_list for char in digits['2']]
                match_three = [char in char_list for char in digits['3']]

                if all(match_two):
                    value.append(2)
                elif all(match_three):
                    value.append(3)
                else:
                    value.append(5)
            
            elif length == 6:
                match_zero = [char in char_list for char in digits['0']]
                match_six = [char in char_list for char in digits['6']]

                if all(match_zero):
                    value.append(0)
                elif all(match_six):
                    value.append(6)
                else:
                    value.append(9)
            
            elif len(digit) == 7:
                value.append(8)

        
        # at this point, value equals something like [4, 6, 2, 3]
        # so, for that example (4 * 1000) + (6 * 100) + (2 * 10) + 3 is the four digit integer equivalent
        # this is appended to values as the value for this row
        values.append(value[0] * 1000 + value[1] * 100 + value[2] * 10 + value[3])

    # the outer loop ends and the sum of the four digit values in values (the list) is returned as the answer
    return sum(values)

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day8_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
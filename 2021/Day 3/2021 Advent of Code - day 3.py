import numpy as np

def parse(input_file):
    """Parse input to 2D Numpy array from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       
    
    def split_to_ints(binary_str):
        """Splits a binary string to a list of integers"""
        return [int(char) for char in binary_str]
    
    # convert to list of lists of integers
    contents_lists = [split_to_ints(x) for x in contents.splitlines()]
   
    # return 2D numpy array from the list of lists.
    # Each row contains the bits for a binary number. 
    # for example 
    # [[1 0 1 1 1]
    # [0 1 0 0 0]]
    return np.array(contents_lists)
    
def solve_part1(diagnostics_np):
    """Function to solve puzzle part 1"""
    
    # swap rows and columns so that row 1 is the first bit of every binary number, row 2 the second bit of every binary number, etc
    transposed_np = diagnostics_np.transpose()

    # find the length of this new array
    total_diagnostics = len(transposed_np[0])
    # create an empty list to store the count of 1 bits for each row of this transposed array
    count_of_ones = []

    # dynamically adjusts for any binary number length (the example data is 5 bits long, the real data is 12 bits long)
    for row in transposed_np:
        # since binary is 1 or 0, count_nonzero counts all the 1 bits
        # the count for that row is appended to the count_of_ones list
        count_of_ones.append(np.count_nonzero(row))

    # empty lists
    gamma_list = []
    epsilon_list = []

    # append string character bits ('1' or '0') for gamma and epsilon ratings expressed as binary 
    # example output could be ['1', '0', '1', '1', '1']
    for count in count_of_ones:
        # if ones are more than half the total number of diagnostic readings
        if count > (total_diagnostics / 2):
            gamma_list.append('1')
            epsilon_list.append('0')
        else:
            gamma_list.append('0')
            epsilon_list.append('1')

    # join the string bits to a string binary number, then convert to decimal integer
    gamma_decimal_int = int("".join(gamma_list), 2)
    epsilon_decimal_int = int("".join(epsilon_list), 2)

    # multiply the two decimal integer values and return this answer
    return gamma_decimal_int * epsilon_decimal_int

def solve_part2(diagnostics_np):
    """Solves puzzle part 2.
    Takes 2D numpy array as input"""

    def find_oxygen_rating(diagnostics_np, char_count):
        """Recursive function to filter out values until one remains.
        At each pass, numbers with the most common bit value at that position are kept.
        Takes a 2D numpy array and the position to be checked (expressed as an integer) as input"""

        # count the number of binary numbers (each binary number expressed as a numpy array row) in the 2d numpy array.
        len_total = len(diagnostics_np)

        if len_total == 1:
            # convert the one remaining element of the numpy array (the final binary number) to list of integers
            oxygen_rating_intlist = diagnostics_np[0].tolist()
            # convert to list of strings
            oxygen_rating_strlist = [str(x) for x in oxygen_rating_intlist]
            # join the list of strings to a single binary number, then convert to a decimal integer and return this value
            return int("".join(oxygen_rating_strlist), 2)

        else:
            # using the numpy array (not transposed - rows and columns in their original orientation)
            # finds the number of 1 bits at horizontal position chat_count for all rows
            len_one = len(diagnostics_np[diagnostics_np[:,char_count] == 1])
        
            # if the number of 1 bits is greater or equal to half the total length of the numpy array
            if len_one >= (len_total / 2):
                # the new 2d numpy array contains the binary numbers (bits making up each row) which have 1 at horizontal position char_count
                new_np = diagnostics_np[diagnostics_np[:,char_count] == 1]
            else:
                # the new 2d numpy array contains the binary numbers (bits making up each row) which have 0 at horizontal position char_count
                new_np = diagnostics_np[diagnostics_np[:,char_count] == 0]
            
            char_count += 1
            # call the function recursively with the new numpy array and looking at the next horizontal position (char_count)
            return find_oxygen_rating(new_np, char_count)

    def find_co2_rating(diagnostics_np, char_count):
        """Recursive function to filter out values until one remains.
        At each pass, numbers with the least common bit value at that position are kept.
        If there are an equal number of 1 and 0 bits, numbers with 0 bit at that position are kept.
        Takes a 2D numpy array and the position to be checked (expressed as an integer) as input"""
        
        len_total = len(diagnostics_np)

        if len_total == 1:
            # base path. convert the one remaining element of np_array to list of ints
            co2_rating_intlist = diagnostics_np[0].tolist()
            # convert to list of strings
            co2_rating_strlist = [str(x) for x in co2_rating_intlist]
            # exit the recursive function by joining the list of strings to a single binary number, then convert to a decimal integer and return this value
            return int("".join(co2_rating_strlist), 2)

        else:
            len_one = len(diagnostics_np[diagnostics_np[:,char_count] == 1])
        
            # if there are an equal number of 0 bits and 1 bits, keep the binary numbers with 0 in that position
            if len_one < (len_total / 2):
                # the new 2d numpy array contains the binary numbers (bits making up each row) which have 1 at horizontal position char_count
                new_np = diagnostics_np[diagnostics_np[:,char_count] == 1]
            else:
                # the new 2d numpy array contains the binary numbers (bits making up each row) which have 0 at horizontal position char_count
                new_np = diagnostics_np[diagnostics_np[:,char_count] == 0]
            
            char_count += 1
            # call the function recursively with the new numpy array and looking at the next horizontal position (char_count)
            return find_co2_rating(new_np, char_count)

    # find the oxygen and co2 ratings
    oxy = find_oxygen_rating(diagnostics_np, 0)
    co2 = find_co2_rating(diagnostics_np, 0)

    # return the product of the oxygen and co2 ratings to solve the puzzle
    return oxy * co2

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day3_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
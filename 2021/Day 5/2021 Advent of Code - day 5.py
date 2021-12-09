import numpy as np

def parse(input_file):
    """Parse input to x from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    lines = contents.splitlines()
    lines = [x.replace(" -> ", ",") for x in lines]
    lines = [x.split(",") for x in lines]
    lines = [[int(x) for x in row] for row in lines]
    
    # 2d numpy array with four columns per row - x1 y1 x2 y2
    return np.array(lines)

def find_horizontal_and_vertical_lines(coordinates):
    # create a grid to map the line positions
    # plus one because a range of 0-9 requires a grid of 10x10
    size = np.amax(coordinates) + 1

    # create a numpy array filled with zeros as integers to the required size (max coordinate value plus one)
    ocean_floor_grid = np.zeros((size, size), dtype=int)

    # loops through each row, containing start and end coordinates
    for row in coordinates:
        # if y1 and y2 are equal
        if row[1] == row[3]:
            # if x1 is less/left of x2
            if row[0] < row[2]:
                # add one to range y, x1:(x2 + 1)
                ocean_floor_grid[row[1],row[0]:row[2]+1] += 1
            # x2 is less/left of x1
            else:
                # add one to range y, x2:(x1 + 1)
                ocean_floor_grid[row[1],row[2]:row[0]+1] += 1
        
        # if x1 and x2 are equal
        elif row[0] == row[2]:
            # if y1 is less/left of y2
            if row[1] < row[3]:
                # add one to range y1:(y2 + 1), x
                ocean_floor_grid[row[1]:row[3]+1,row[0]] += 1
            # y2 is less/left of y1
            else:
                # add one to range y2:(y1 + 1), x
                ocean_floor_grid[row[3]:row[1]+1,row[0]] += 1
    
    return ocean_floor_grid

def find_diagonal_lines(coordinates):
    # create a grid to map the line positions
    # plus one because a range of 0-9 requires a grid of 10x10
    size = np.amax(coordinates) + 1

    # create a numpy array filled with zeros as integers to the required size (max coordinate value plus one)
    ocean_floor_grid = np.zeros((size, size), dtype=int)

    # loops through each row, containing start and end coordinates
    for row in coordinates:
        # if neither y1 and y2 nor x1 and x2 are equal
        if row[1] != row[3] and row[0] != row[2]:
            
            # distance is the same for each axis, so just calculate for x axis
            distance = abs(row[2]-row[0])
            
            # add one to the starting coordinate
            ocean_floor_grid[row[1],row[0]] += 1

            # amount
            i = 1

            # diagonally up and right
            if row[1] < row[3] and row[0] < row[2]:
                while i <= distance:
                    ocean_floor_grid[row[1] + i,row[0] + i] += 1
                    i += 1
            
            # diagonally down and right
            elif row[1] > row[3] and row[0] < row[2]:
                while i <= distance:
                    ocean_floor_grid[row[1] - i,row[0] + i] += 1
                    i += 1

            #diagonally up and left
            elif row[1] < row[3] and row[0] > row[2]:
                while i <= distance:
                    ocean_floor_grid[row[1] + i,row[0] - i] += 1
                    i += 1
            
            # diagonally down and left
            else:
                while i <= distance:
                    ocean_floor_grid[row[1] - i,row[0] - i] += 1
                    i += 1
    
    return ocean_floor_grid

def solve_part1(coordinates):
    """Solves puzzle part 1."""

    ocean_floor_grid = find_horizontal_and_vertical_lines(coordinates)

    # return a sum (count) of the number of elements that evaluate True to being greater than or equal to 2
    return (ocean_floor_grid >= 2).sum()

def solve_part2(coordinates):
    """Solves puzzle part 2."""

    ocean_floor_grid = find_horizontal_and_vertical_lines(coordinates) + find_diagonal_lines(coordinates)

    # return a sum (count) of the number of elements that evaluate True to being greater than or equal to 2
    return (ocean_floor_grid >= 2).sum()

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day5_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
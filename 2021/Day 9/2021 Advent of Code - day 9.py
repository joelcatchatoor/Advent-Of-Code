import numpy as np

def parse(input_file):
    """Parse input to 2D NumPy array from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read() 

        lines = contents.splitlines()

        return np.array([[int(x) for x in line] for line in lines])        

def solve_part1(floor_readings_array):
    """Solves puzzle part 1.
    Finds all low points by comparing every value to its adjacent values (right, left, down and up).
    returns sum of all low points plus 1 for each low point (calculated using len()).
    """

    low_points = []

    # For each reading in the floor_readings_array, builds a list of its adjacent readings (right, left, down and up), if they exist.
    for ind_y, row in enumerate(floor_readings_array):
        for ind_x, reading in enumerate(row):
            adjacencies = []
            
            if ind_x + 1 < floor_readings_array.shape[1]:
                adjacencies.append(floor_readings_array[ind_y][ind_x + 1])
            if ind_x - 1 >= 0:
                adjacencies.append(floor_readings_array[ind_y][ind_x - 1])
            if ind_y + 1 < floor_readings_array.shape[0]:
                adjacencies.append(floor_readings_array[ind_y + 1][ind_x])
            if ind_y - 1 >= 0:
                adjacencies.append(floor_readings_array[ind_y - 1][ind_x])
            
            # Compares reading against its adjacent readings to see if reading is less than them all. If it is, reading is added to low_points list.
            if all(i > reading for i in adjacencies):
                low_points.append(reading)
            
    # risk level for each low point equals 1 + height (its value). len() adds 1 for every low point.
    return len(low_points) + sum(low_points)

def solve_part2(floor_readings_array):
    """Solves puzzle part 2.
    Starts by mapping the floor readings to a boolean array, where the 9's are True (& everything else is False).
    Defines a flood fill function that counts the number of places in a basin & which updates visited places to True in the boolean array. Returns a list of 1's.
    Loops through the boolean array, looking for starter positions to analyse a new basin, then adding each basin size to a list of basins.
    Finds the largest three basins (by size).
    Returns the product of the largest three basins.
    * Flood fill: https://www.freecodecamp.org/news/flood-fill-algorithm-explained-with-examples/ (accessed December 2021)
    """

    # bool array of shape floor readings array, False except if equal to 9, then True (to start)
    assessed_places = floor_readings_array == 9
    
    def flood_fill(assessed_places, ind_y, ind_x, basin):
        """Counts the number of places in a basin"""
        if ind_y == -1 or ind_x == -1 or ind_y == assessed_places.shape[0] or ind_x == assessed_places.shape[1]:
            return
        
        if assessed_places[ind_y][ind_x] == True:
            return
        
        # in truth, I got frustrated unsuccessfully using integer += 1 in this resursive function because I knew I wasn't storing it correctly as it didn't output the indended value. Using a list it behaves as I desired.
        basin.append(1)
        # mark that the function has now been here, to avoid any double counting
        assessed_places[ind_y][ind_x] = True

        # call function again to look right, left, down, up respectively
        flood_fill(assessed_places, ind_y, ind_x + 1, basin)
        flood_fill(assessed_places, ind_y, ind_x - 1, basin)
        flood_fill(assessed_places, ind_y + 1, ind_x, basin)
        flood_fill(assessed_places, ind_y - 1, ind_x, basin)

        return basin

    # empty list of basins
    basins = []

    # loops through the assessed_places array
    for ind_y, row in enumerate(assessed_places):
        for ind_x, x in enumerate(row):
            # if the place is unvisited (and is not equal to 9)
            if x == False:
                # add to basins the sum of this basin list e.g. sum([1, 1, 1]) = basin of size 3 for the current place and its adjacent neighbours (plus their neighbours... etc)
                basins.append(sum(flood_fill(assessed_places, ind_y, ind_x, [])))
    
    # convert to NumPy array
    basins_np = np.array(basins)

    # locate the indexes of the largest three basins (by size)
    largest_three_ind = np.argpartition(basins_np, -3)[-3:]

    # save the values of the largest three basin sizes
    largest_basins = basins_np[largest_three_ind]

    # return the product of the largest three basin sizes
    return np.prod(largest_basins)

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day9_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
import numpy as np

def parse(input_file):
    """Parse input to x from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()  

    list = contents.splitlines()
    list_of_lists = [[int(x) for x in line] for line in list]
    
    array = np.array(list_of_lists)
    return np.pad(array, 1)

def step(octo_np, flashes):       

    octo_np += 1
    flashed_this_step = np.zeros((11,11), dtype=bool)
    
    def flash(octo_np, flashed_this_step, ind, flashes):
        if ind[0] <= 0 or ind[1] <= 0 or ind[0] >= 11 or ind[1] >= 11:
            return octo_np, flashes, flashed_this_step
        
        if octo_np[ind] > 9 and flashed_this_step[ind] == False:

            octo_np[ind[0]-1:ind[0]+2,ind[1]-1:ind[1]+2] += 1
            flashed_this_step[ind] = True
            flashes += 1

            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] - 1, ind[1]), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] - 1, ind[1] - 1), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] - 1, ind[1] + 1), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0], ind[1] - 1), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0], ind[1] + 1), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] + 1, ind[1]), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] + 1, ind[1] - 1), flashes)
            octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, (ind[0] + 1, ind[1] + 1), flashes)
        
        return octo_np, flashes, flashed_this_step

    for ind, x in np.ndenumerate(octo_np):
        octo_np, flashes, flashed_this_step = flash(octo_np, flashed_this_step, ind, flashes)

    for ind, x in np.ndenumerate(octo_np):
        if x > 9:
            octo_np[ind] = 0

    return octo_np, flashes 

def solve_part1(octo_np, steps):
    """Solves puzzle part 1."""

    i = 0
    flashes = 0

    while i < steps:
        octo_np, flashes = step(octo_np, flashes)
        i += 1
    
    return flashes

def solve_part2(octo_np):
    """Solves puzzle part 2."""
    
    i = 0
    flashes = 0

    while True:
        octo_np, flashes = step(octo_np, flashes)
        i += 1
        
        if np.all(octo_np[1:11,1:11] == 0):
            break
    
    return i

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)
    
    # part1 was mutating the NumPy array ahead of its use by part2 (result was that if steps was n above 0, the answer to part2 would be reduced by n, since it would take x - n days to reach synchronisation).
    # therefore, this copy of the original NumPy array is passed to part2.
    data2 = np.copy(data)

    steps = 100
 
    return solve_part1(data, steps), solve_part2(data2)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day11_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
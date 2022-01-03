import collections

def parse(input_file):
    """Parse input to adjacency list as dictionary from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    # splits text file to a list of strings, where each string is a line of the text file
    lines = contents.splitlines()
    # splits each line e.g. ["'start'-'A'",...] to [['start','A'],...]
    list_of_lists = [x.split("-") for x in lines]
    # stores unique values
    # flattens list of lists to list then converts to a set, thus removing duplicates 
    # flattening list of lists: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    nodes = set([x for sublist in list_of_lists for x in sublist])

    # starts to create an adjacency list using a dictionary
    # uses the unique values in set 'nodes' as keys
    adj_list = dict.fromkeys(nodes, [])

    # adds adjacencies to each key
    for key in adj_list.keys():
        
        adjs = []
        
        for list in list_of_lists:
            # adds adjacency regardless of which order the nodes were listed in the original data
            if key == list[0]:
                adjs.append(list[1])
            if key == list[1]:
                adjs.append(list[0])
        
        adj_list[key] = adjs
    
    # returns adjacency list as dictionary
    return adj_list

def find_paths(adj_list, lower_twice=False):
    """Finds all paths from 'start' to 'end', where either:
        - no lower case named caves can be visited twice; or
        - only one lower case named cave can be visited twice."""
    # list of lists, storing all paths from 'start' to 'end'.
    paths = []  
    # stack to store paths that still need to be considered and acted on.
    stack_paths = [] 

    # populate the stack with initial options
    for adj in adj_list['start']:
        stack_paths.append(['start', adj])
    
    # loop through stack_paths until all options are exhausted (stack_paths is 0, i.e. False)        
    while stack_paths:
        # pop the path in progress to work with for this iteration of the loop
        current_path = stack_paths.pop()
        # store the current cave
        cave = current_path[-1]

        # add path to paths if cave equals end and if the current path is not in paths already. continue to next while loop iteration.
        if cave == 'end':
            if current_path not in paths:
                paths.append(current_path)
                continue
            else:
                continue
        
        if lower_twice == True:
            # count the frequency of all elements (caves) in current path
            count = collections.Counter(current_path)
            # filter the count to caves where the name is lower case and where it appears twice (or more)
            filtered_count = {k:v for (k,v) in count.items() if v > 1 and k.islower()}
            # count the number of items that match this filtered criteria
            len_filtered_count = len(filtered_count)

        # loop through the adjacent caves to the current cave using the adjacency list
        for adj in adj_list[cave]:
            # if the adjacent cave is lower and is already in the current path    
            if adj in current_path and adj.islower():
                
                # handles paths where one lower case named cave can be visited twice
                if lower_twice == True:
                    # if the adjacent cave is neither start nor end and if no lower cased named cave is already in current_path twice (or more)
                    if adj not in {'start', 'end'} and len_filtered_count == 0:
                        # allow the duplication to be added to current path create a new path
                        new_path = current_path + [adj]
                    else:
                        continue
                
                # if lower_twice == False, i.e. no lower case named caves can be visited twice
                else:
                    continue
            
            # otherwise, either it's an upper cased named cave or it's lower case but not already in the current path
            # this means it can be added to current path to make the new path
            else:
                new_path = current_path + [adj]
                    
            # append the new path (of this for loop iteration) to the stack
            stack_paths.append(new_path)
        
    # once the while loop finishes, return paths
    return paths

def solve_part1(adj_list):
    """Solves puzzle part 1."""
    
    paths = find_paths(adj_list)

    return len(paths)

def solve_part2(adj_list):
    """Solves puzzle part 2."""

    # one lower case named cave per path can be visited twice (lower_twice=True)
    paths = find_paths(adj_list, True)
            
    # return count of paths 
    return len(paths)

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day12_exampleinput1.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
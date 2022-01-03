def parse(input_file):
    """Parse input to adjacency list as dictionary from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       

    lines = contents.splitlines()

    list_of_lists = [x.split("-") for x in lines]

    nodes = set([x for sublist in list_of_lists for x in sublist])

    adj_list = dict.fromkeys(nodes, [])

    for key in adj_list.keys():
        
        adjs = []
        
        for list in list_of_lists:
            if key == list[0]:
                adjs.append(list[1])
            if key == list[1]:
                adjs.append(list[0])
        
        adj_list[key] = adjs
    
    # returns adjacency list as dictionary
    return adj_list

def solve_part1(adj_list):
    """Solves puzzle part 1."""
    paths = []  
    stack_paths = [] 

    for adj in adj_list['start']:
        stack_paths.append(['start', adj])
    
    while stack_paths:
        current_path = stack_paths.pop()
        cave = current_path[-1]

        if cave == 'end' and current_path not in paths:
            paths.append(current_path)
            continue

        for adj in adj_list[cave]:
            if adj in current_path and adj.islower():
                continue
            else:
                new_path = current_path + [adj]
            
            stack_paths.append(new_path)

    # iterative version of a depth first algorithm, where a given path is up to 13 elements in length
    # tried recursion first: it exceeded python's default recursion limit
    # level 0 - neighbours (adjacency, adj) of 'start'
    
    
    
    
    """
    for adj in adj_list['start']:
        path = ['start'] + [adj]

        if adj == 'end':
            paths.append(path)
            continue
        else:
            # level 1 
            for adj_1 in adj_list[adj]:
                path_1 = path + [adj_1]

                if adj_1 == 'end':
                    paths.append(path_1)
                    continue
                elif adj_1 in path and adj_1.islower():
                    continue
    """            
    

    # recursive version (DFS) that exceeded Python's default recursion limit
    """
    def find_path(path, node)    
        for adj in adj_list[node]:
        
            if adj == 'end':
                path.append(adj)
                paths.append(path)
                return

            if adj.islower():
                if adj in path:
                    return
                else:
                    path.append(adj)
                    for neighbour in adj_list[adj]:
                        find_path(path, neighbour)
                    return
            
            # if is upper (by process of elimination)
            if adj.isupper():
                path.append(adj)
                for neighbour in adj_list[adj]:
                    find_path(path, neighbour)
                return
    
    
    find_path([], 'start')
    """

    return len(paths)

def solve_part2(data):
    """Solves puzzle part 2."""

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day12_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
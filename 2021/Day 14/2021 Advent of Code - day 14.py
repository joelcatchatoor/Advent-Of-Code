from copy import deepcopy
import collections

# Acknowledgement (accessed 5th January 2022): late stage reference for expressing what I wanted to express in code: https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/hoib78w/

def parse(input_file):
    """Parse input to tuple of a Counter and two dictionaries from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read() 

    # split the polymer template and the pair insertion rules (empty line)
    contents = contents.split("\n\n")
    
    template_str = contents[0]

    # count the frequency of adjacent element pairs in the polymer template, store as a Counter     
    template = collections.Counter(a+b for a,b in zip(template_str,template_str[1:]))

    # split the insertion rule text into list of lines
    insertion_rule_lines = contents[1].splitlines()
    # dictionary comprehension to select the relevant characters from each line in key value pairs e.g. AB: C
    rules = {x[:2]:x[6] for x in insertion_rule_lines}
    
    # count the frequency of each unique element.
    elements = collections.Counter(template_str)

    return template, rules, elements

def pair_insertion(template, rules, elements, steps):
    """Solves puzzle parts."""

    current_template = template

    for _ in range(steps):
        new_template = collections.Counter()
        
        # loop through the current template. e.g. key is NB
        for key in current_template.keys():
            # check key against the keys of the rules dictionary
            if key in rules:
                # looks up the element to insert e.g. C
                element_to_insert = rules[key]
                # looks up the current value (count of) the key e.g. 26
                amount = current_template[key]
                
                # add the amount to the element value, since it will have been inserted that many times
                # e.g. C += 26
                elements[element_to_insert] += amount

                # use string concatenation to access/create the two new adjacent pairs in the new_template Counter dictionary following the insertion of the new element e.g. NC and CB
                # add the amount to their value in the new template dictionary, since the new adjacent pairs will have been created that many times
                # e.g. NC += 26
                new_template[key[0] + element_to_insert] += amount
                # e.g. CB += 26
                new_template[element_to_insert + key[1]] += amount

        # make the new template the template to loop over in the next iteration
        current_template = new_template

    # find the largest and smallest values in elements and return their difference
    return max(elements.values()) - min(elements.values())

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)
    # deepcopy the data to make sure the two function calls operate independently
    # tuples are immutable but can contain mutable objects. deepcopy manages this.
    data2 = deepcopy(data)

    part1 = pair_insertion(data[0], data[1], data[2], 10)
    part2 = pair_insertion(data2[0], data2[1], data2[2], 40)

    return part1, part2 

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day14_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
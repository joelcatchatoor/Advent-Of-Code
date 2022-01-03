def parse(input_file):
    """Parse input to x from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()

        return contents.splitlines()       

def check_for_incorrect_chars(line):
    brackets = []
    
    for char in line:
        if char in ["[","{","(","<"]:
            brackets.append(char)
        else:
            if brackets[-1] == "[" and char != "]":
                    return char
            elif brackets[-1] == "{" and char != "}":
                    return char
            elif brackets[-1] == "(" and char != ")":
                    return char
            elif brackets[-1] == "<" and char != ">":
                    return char
            
            brackets.pop()

    # if no incorrect characters are found, return string "none"
    return "none"

def find_missings_chars(line):
    
    brackets = []

    for char in line:
        if char in ["[","{","(","<"]:
            brackets.append(char)
        else:
            if brackets[-1] == "[" and char == "]":
                    brackets.pop()
            elif brackets[-1] == "{" and char == "}":
                    brackets.pop()
            elif brackets[-1] == "(" and char == ")":
                    brackets.pop()
            elif brackets[-1] == "<" and char == ">":
                    brackets.pop()
            
    brackets.reverse()

    for ind, char in enumerate(brackets):
        if brackets[ind] == "[":
            brackets[ind] = "]"
        elif brackets[ind] == "{":
            brackets[ind] = "}"
        elif brackets[ind] == "(":
            brackets[ind] = ")"
        elif brackets[ind] == "<":
            brackets[ind] = ">"

    print(brackets)
    return brackets

def solve_part1(lines):
    """Solves puzzle part 1."""

    incorrect_chars = []

    for line in lines:
        incorrect_chars.append(check_for_incorrect_chars(line))
    
    print(incorrect_chars)
    score = 0

    for char in incorrect_chars:
        if char == ")":
            score += 3
        elif char == "]":
            score += 57
        elif char == "}":
            score += 1197
        elif char == ">":
            score += 25137
    
    return score

def solve_part2(lines):
    """Solves puzzle part 2."""

    scores = []
    
    for line in lines:
        if check_for_incorrect_chars(line) != "none":
            continue

        missing_chars = find_missings_chars(line)
        score = 0

        for char in missing_chars:
            if char == ")":
                score = (score * 5) + 1
            elif char == "]":
                score = (score * 5) + 2
            elif char == "}":
                score = (score * 5) + 3
            elif char == ">":
                score = (score * 5) + 4
        
        scores.append(score)
    
    scores.sort()

    return scores[len(scores) // 2]

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data), solve_part2(data)

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day10_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
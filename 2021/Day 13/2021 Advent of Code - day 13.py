import numpy as np
from PIL import Image, ImageFilter
import pytesseract

def parse(input_file):
    """Parse input to x from text file"""
    # open input text file and save contents
    with open(input_file) as input:
        contents = input.read()       
    
    # seperate the contents of the text file into its two sections, coordinates and folding instructions. The sections are separated by an empty line.
    separate = contents.split("\n\n")

    # the text file coordinates are x,y. NumPy is y,x - so split, convert to int, reverse and make each coordinate pair a tuple
    coordinates = separate[0].splitlines()
    coordinates = [x.split(",") for x in coordinates]
    coordinates = [[int(x) for x in pair] for pair in coordinates]
    coordinates = [pair[::-1] for pair in coordinates]
    coordinates = [tuple(pair) for pair in coordinates]

    # remove additional text and store either 'y' or 'x' then the value as an int. e.g. 'y', 7
    folds = separate[1].splitlines()
    folds = [x.replace("fold along ","") for x in folds]
    folds = [x.split("=") for x in folds]
    folds = [[x[0],int(x[1])] for x in folds]

    # find largest coordinate size for y
    y_coords = [pair[0] for pair in coordinates]
    y_coords.sort()
    largest_y = y_coords[-1]

    # find largest coordinate size for x
    x_coords = [pair[1] for pair in coordinates]
    x_coords.sort()
    largest_x = x_coords[-1]

    # create boolean array of size largest y + 1, largest x + 1 that is all False
    bool_array = np.zeros((largest_y+1,largest_x+1), dtype=bool)

    # marks as True for each coordinate pair, using them as an index for the array
    for pair in coordinates:
        bool_array[pair] = True

    return bool_array, folds

def fold_left(bool_array, x):
    """Folds everything right of x over and onto everything left of x"""

    right = bool_array[:,x+1:]
    left = bool_array[:,:x]

    # horizontal flip (or mirror) of the array has the effect of folding over
    right_flipped = np.fliplr(right)

    # add two arrays together (the effect being Trues added where previously False) 
    # ensures the two arrays are of equal size and are aligned to the fold line
    if np.size(right_flipped, 1) < np.size(left, 1):
        new_array = left.copy()
        # start the horizontal (x axis) from the difference between the larger array and the smaller array
        new_array[:,np.size(left, 1) - np.size(right_flipped,1):] += right_flipped
    else:
        new_array = right_flipped.copy()
        # start the horizontal (x axis) from the difference between the larger array and the smaller array
        new_array[:,np.size(right_flipped, 1) - np.size(left,1):] += left  

    return new_array

def fold_up(bool_array, y):
    """Folds everything lower than y up and onto everything up of y"""

    lower = bool_array[y+1:,:]
    upper = bool_array[:y,:]

    # vertical flip (or mirror) of the array has the effect of folding over
    lower_flipped = np.flipud(lower)

    # add two arrays together (the effect being Trues added where previously False) 
    # ensures the two arrays are of equal size and are aligned to the fold line
    if np.size(lower_flipped, 0) < np.size(upper, 0):
        new_array = upper.copy()
        # start the vertical (y axis) from the difference between the larger array and the smaller array
        new_array[np.size(upper, 0) - np.size(lower_flipped,0):,:] += lower_flipped
    else:
        new_array = lower_flipped.copy()
        # start the vertical (y axis) from the difference between the larger array and the smaller array
        new_array[np.size(lower_flipped, 0) - np.size(upper,0):,:] += upper  

    return new_array

def solve_part1(bool_array, folds):
    """Solves puzzle part 1. 
    - Performs the first folding instruction in the data file
    - returns a count of the Trues following this instruction.
    """

    if folds[0][0] == 'x':
        folded_array = fold_left(bool_array, folds[0][1])
    else:
        folded_array = fold_up(bool_array, folds[0][1])

    return np.count_nonzero(folded_array)

def solve_part2(bool_array, folds):
    """Solves puzzle part 2. 
    - Follows all folding instructions in the data file
    - converts the final Numpy array to an image, to see the characters spelled out by the pattern of 'Trues' amongst the 'Falses'. 
    - pre-processes the image to prepare for OCR
    - Uses OCR (pytesseract) to read and return the eight characters spelled out in the image.
    """

    # duplicate boolean array
    folded_array = bool_array.copy()

    # work through the folding instructions
    for fold in folds:
        if fold[0] == 'x':
            folded_array = fold_left(folded_array, fold[1])
        else:
            folded_array = fold_up(folded_array, fold[1])

    # convert final array to an image to start to identify the eight capital letters which the patterns in the array spell out.
    # produces an image with a black background and white foreground
    im = Image.fromarray(folded_array)

    # image processing to upscale and smooth the very low resolution, pixelated image into more readable characters
    # 1. find size (e.g. 40x6)
    width, height = im.size
    
    # 2. add padding to improve OCR performance. Create a new image that's bigger, then paste the original image on top of it
    im_pad = Image.new('1', (width * 2, height * 2), 0)
    # note: OCR performance was better if the text was aligned bottom
    im_pad.paste(im, ((width * 2 - width) // 2, height))

    # 3. convert to grayscale to allow for resizing (with bicubic resampling) and blurring
    im_gray = im_pad.convert('L')

    # 4. resize to improve OCR performance. Resampling begins to join up the pixelated diagonals.
    im_big = im_gray.resize((width * 100, height * 100), Image.BICUBIC)

    # 5. apply a blur to further smooth & join up the pixelated diagonals
    im_blur = im_big.filter(ImageFilter.GaussianBlur(12))

    # 6. convert to black and white, and invert the colours
    # this 'bakes in' the smoothing and joining up which was achieved by the blurring and resampling
    # black text on a white background (achieved through inversion) helps improve OCR performance
    im_inverted = im_blur.point(lambda x: 255 if x<85 else 0, '1')

    # Use Optical Character Recognition (OCR) to read the eight character code from the image
    # config tells Tesseract to treat the image as a single text line, for improved OCR performance
    code = pytesseract.image_to_string(im_inverted, lang='eng', config='--psm 7')

    # remove any spaces and return the eight character code spelled out in the image
    return code.replace(" ", "")

def solve(input_file):
    """Solve the two-part puzzle for the input provided"""
    data = parse(input_file)

    return solve_part1(data[0], data[1]), solve_part2(data[0], data[1])

if __name__ == "__main__":
    # set the input file path (assume the input file is in the same directory)
    # designed to test with example data first
    input_file = 'day13_input.txt'
    
    # solve the two-part puzzle and store the answers
    answers = solve(input_file)
    
    # print the answers
    print("Part 1 answer: " + str(answers[0]))
    print("Part 2 answer: " + str(answers[1]))
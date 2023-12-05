# Advent of Code Day 1 Challenge 2023

## Overview

This repository contains a Python solution for the Advent of Code Day 1 Challenge, 2023. The challenge, a two-part problem, involves parsing a calibration document with altered text to extract specific calibration values.

## Challenge Summary

The Elves' crucial calibration document for global snow production has been inadvertently amended by a young Elf. The task is to process this document to recover calibration values from each line of text. These values are derived by combining the first and last digits (or their spelled-out equivalents) on each line to form a two-digit number.

## Solution

The script can address both parts of this two-part challenge:
1. **Part 1:** Focuses on lines containing direct numeric digits.
2. **Part 2:** Extends the solution to include digits (one-nine) spelled out as words (e.g., 'one', 'two', etc.).

### Key Features

- Handles both direct digits and their spelled-out versions.
- Uses regular expressions for efficient pattern recognition.

### Note

To cater to edge cases like 'oneight' being 18, the script employs two `re.search` operations per line — one with the line (a string) in its original direction and one in reverse — ensuring the accurate identification of digits.

## Usage

1. Ensure Python 3.x is installed on your system.
2. Place your calibration document text file (default is 'day1_input.txt') in the same directory as the script.
3. Update the PART2 constant to True or False depending whether you want to solve part 1 or part 2 of the coding challenge.
4. Execute the script using the command: `python3 [script_name].py`.

## Dependencies

This script uses Python's standard library only.

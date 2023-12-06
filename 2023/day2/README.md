# Advent of Code Day 2 Challenge 2023

## Overview
This repository contains a Python solution for the Advent of Code Day 2 Challenge, 2023. The challenge, titled "Cube Conundrum," is a two-part problem that involves determining the possible configuration of coloured cubes in a bag based on revealed subsets of cubes.

## Challenge Summary
The challenge is set on Snow Island, where you play a game with an Elf. The game involves a bag containing red, green, and blue cubes. In each round, the Elf reveals a subset of cubes, and your goal is to deduce information about the total number of cubes in the bag.

- **Part 1**: Identify which games could be possible given a specific number of each colour cube in the bag.
- **Part 2**: Determine the fewest number of cubes of each colour that must have been in the bag for each game to be possible.

## Solution
The Python script addresses both parts of this two-part challenge:

- **Part 1**: The script calculates the sum of the IDs of the games that are possible with a given number of cubes.
- **Part 2**: It then determines the minimum number of cubes required for each game and calculates the 'power' of these sets.

## Key Features
- Efficient parsing of input data using regular expressions.
- Calculation of the minimum set of cubes and their 'power' for each game.
- Well-structured and modular code for easy readability and maintenance.

## Usage
- Ensure Python 3.x is installed on your system.
- Place your puzzle input text file (default is 'day2_input.txt') in the same directory as the script.
- Execute the script using the command: `python3 [script_name].py`.

## Dependencies
This script relies solely on Python's standard library.

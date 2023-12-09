# Advent of Code Day 3 Challenge 2023

## Overview
This repository contains the Python solution for the Advent of Code Day 3 Challenge 2023, titled "Gear Ratios." The challenge involves analysing an engine schematic to identify and sum up part numbers and gear ratios.

## Challenge Summary
The challenge is set in a fictional scenario where you're tasked with fixing a gondola lift by identifying missing or incorrect parts in its engine. The engine schematic is presented as a grid of numbers and symbols, and your task is divided into two parts:

- **Part 1**: Sum all the "part numbers" in the engine schematic. A part number is defined as any number adjacent to a symbol in the schematic.
- **Part 2**: Calculate the gear ratios for specific gears in the engine. A gear is identified as a `*` symbol adjacent to exactly two part numbers, and its gear ratio is the product of these two numbers.

## Solution
The Python script provides a solution for both parts of the challenge:

- **Part 1**: It iterates through the grid to find and sum up all part numbers.
- **Part 2**: It identifies gears in the grid and calculates their gear ratios, summing them up to identify the incorrect gear.

## Key Features
- Parsing the engine schematic from a text file.
- Grid traversal and identification of part numbers and gears.
- Calculation of gear ratios and summing them to find the solution.
- Documentation through docstrings and type hints.

## Usage
- Make sure Python 3.x is installed on your system.
- The script expects an input file named 'day3_input.txt' in the same directory. This file should contain the engine schematic.
- Run the script using the command: `python3 [script_name].py`.

## Dependencies
The script is self-contained and only uses Python's standard library.

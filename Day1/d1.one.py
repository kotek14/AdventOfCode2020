#!/usr/bin/env python3

# Reading lines from input
expensesFile = "day1.input"
expensesHandle = open(expensesFile, "r")
expensesNumbersStr = expensesHandle.readlines()
expensesHandle.close()

expensesNumbers = []

for expensesNumber in expensesNumbersStr:
    expensesNumbers.append(int(expensesNumber))
# And storing every line as an integer.

for firstNumber in expensesNumbers:
    for secondNumber in expensesNumbers:
        total = firstNumber + secondNumber
        if total == 2020:
            print("The pair is " + str(firstNumber) + " and " + str(secondNumber))
            print("Puzzle answer: " + str(firstNumber * secondNumber))
            exit(0)

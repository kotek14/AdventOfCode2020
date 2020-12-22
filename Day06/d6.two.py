#!/usr/bin/env python3

# How many unique characters are in each group?
# Groups are separated with blank lines.

# First we read our input
fileName = "day6.input"
groupsFileHandle = open(fileName, "r")
groupsTemp = groupsFileHandle.read()
groupsFileHandle.close()
groupsData = groupsTemp.split("\n\n")

# groupsData is a list containing every group string (including newlines)
# we split() each group and see if len(whatever we got) > 1.
# It's easier to set up a function

# Cool. It works as intended.
# This problem made me think. Result: now I know about map().
# https://www.tutorialspoint.com/find-common-elements-in-list-of-lists-in-python

def countCommons(group):
    tempList = []
    splitted = group.split()
    if len(splitted) == 1:
        return(len(splitted[0]))
    for person in splitted:
        tempList.append(list(person))
    common = list(set.intersection(*map(set, tempList)))
    return(len(common))

value = 0

for group in groupsData:
    value += countCommons(group)

print(value)

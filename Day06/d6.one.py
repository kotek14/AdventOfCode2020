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
# we don't really care about newlines. In fact, we need to remove them.
# Then I just use set() to remove duplicates and add the number of characters to value.

value = 0

for group in groupsData:
    temp = list(group)
    while '\n' in temp:
        temp.remove("\n")
    value += len(set(temp))

print(value)

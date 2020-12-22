#!/usr/bin/env python3

# Basic reading from file
mapFileName = "day3.input"
mapHandle = open(mapFileName, "r")
rows = mapHandle.readlines()
mapHandle.close()

i = 0
counter = 0

for row in rows:
    row = row[0:-1]             # Remove the newline at the end
    while len(row) - 2 < i:     # If I'll go out of bounds, double the line length
        row = row * 2           # It doesn't scale well, but does the job WAY better than pregenerating the map.
    if row[i] == '#':           # If it's a tree,
        counter = counter + 1   # increment the counter
    i = i + 3

print(counter)

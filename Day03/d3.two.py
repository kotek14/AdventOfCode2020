#!/usr/bin/env python3

# Basic reading from file
mapFileName = "day3.input"
mapHandle = open(mapFileName, "r")
rows = mapHandle.readlines()
mapHandle.close()

# I mean... It's easy to just... You know... Write 4 more loops.
# Is there a smarter way? Probably. Will come back to it later and figure it out.

i = 0
counter = 0

for row in rows:
    row = row[0:-1]
    while len(row) - 2 < i:
        row = row * 2
    if row[i] == '#':
        counter = counter + 1
    i = i + 3

print(counter)

i = 0
counter = 0

for row in rows:
    row = row[0:-1]
    while len(row) - 1 < i:
        row = row * 2
    if row[i] == '#':
        counter = counter + 1
    i = i + 1

print(counter)

i = 0
counter = 0

for row in rows:
    row = row[0:-1]
    while len(row) - 4 < i:
        row = row * 2
    if row[i] == '#':
        counter = counter + 1
    i = i + 5

print(counter)

i = 0
counter = 0

for row in rows:
    row = row[0:-1]
    while len(row) - 6 < i:
        row = row * 2
    if row[i] == '#':
        counter = counter + 1
    i = i + 7

print(counter)

i = 0
counter = 0

for row in rows[::2]: # Every other item
    row = row[0:-1]
    while len(row) - 1 < i:
        row = row * 2
    if row[i] == '#':
        counter = counter + 1
    i = i + 1

print(counter)

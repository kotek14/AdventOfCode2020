#!/usr/bin/env python3

passwdFile = 'day2.input'
passwdHandle = open(passwdFile, "r")
passwdRules = passwdHandle.readlines()
passwdHandle.close()

validLines = 0

# if characterOnFirstPosition == characterSpecified
# XOR
# characterOnFirstPosition == characterSpecified

for rule in passwdRules:
    words = rule.split()
    positions = words[0].split('-')
    if (words[2][int(positions[0]) - 1] == words[1]) ^ (words[2][int(positions[1]) - 1] == words[1]):
        validLines += 1

print("Puzzle answer: " + str(validLines))

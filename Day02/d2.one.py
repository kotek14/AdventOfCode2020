#!/usr/bin/env python3

passwdFile = 'day2.input'
passwdHandle = open(passwdFile, "r")
passwdRules = passwdHandle.readlines()
passwdHandle.close()

validLines = 0

# words[2] is a password string
# words[1] is a character specified
# limits[0] is the smallest number of occurences
# limits[1] is the biggest number of occurences

for rule in passwdRules:
    words = rule.split()
    limits = words[0].split('-')
    if words[2].count(words[1]) >= int(limits[0]) and words[2].count(words[1]) <= int(limits[1]):
        validLines += 1

print("Puzzle answer: " + str(validLines))

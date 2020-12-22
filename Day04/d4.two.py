#!/usr/bin/env python3

import re # for checking the hex color regex
          # i can use regex more than once but I already wrote most of it

#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.

def checkValueValidity(name, value):
    validNames = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    if name == 'byr':
        try:
            if int(value) >= 1920 and int(value) <= 2002:
                return True
        except:
            return False
    elif name == 'iyr':
        try:
            if int(value) >= 2010 and int(value) <= 2020:
                return True
        except:
            return False
    elif name == 'eyr':
        try:
            if int(value) >= 2020 and int(value) <= 2030:
                return True
        except:
            return False
    elif name == 'hgt':
        if len(value) == 4 and value[-2:] == 'in':
            try:
                if int(value[:2]) >= 59 and int(value[:2]) <= 76:
                    return True
            except:
                return False
        elif len(value) == 5 and value[-2:] == 'cm':
            try:
                if int(value[:3]) >= 150 and int(value[:3]) <= 193:
                    return True
            except:
                return False
    elif name == 'hcl':
        # God save Stackoverflow
        if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', value):
            return True
    elif name == 'ecl':
        validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in validEyeColors:
            return True
    elif name == 'pid':
        if len(value) == 9:
            try:
                int(value)
                return True
            except:
                return False
    elif name == 'cid':
        return True
    return False

validCounter = 0
invalidCounter = 0

passFileName = "day4.input"
passFileHandle = open(passFileName, "r")
passData = passFileHandle.read()
passFileHandle.close()

passports = passData.split("\n\n")
print("Total passports loaded: " + str(len(passports)))

# Now every passport is a separate string item in the passports list.

for passport in passports:
    checkingFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    fields = passport.split()
    for field in fields:
        name = field.split(":")[0]
        value = field.split(":")[1]
        if checkValueValidity(name, value):
            checkingFields.remove(name)
        else: # Another ugly hack that will just generate one or more extra fields if stuff is invalid
            checkingFields.append("error")
    if len(checkingFields) == 0 or (len(checkingFields) == 1 and checkingFields[0] == 'cid'):
        print("Valid password processed!")
        validCounter = validCounter + 1
    else:
        print("Invalid passport denied!")
        invalidCounter = invalidCounter + 1

print("-----------------------------")
print("Valid: " + str(validCounter))
print("Invalid: " + str(invalidCounter))

#!/usr/bin/env python3

# I'm too lazy to clean up code now, so I'll just upload it as is, with my comments and debugging prints.

# Easy.
# - Read all passports
# - Split them on every two lines
# - Split every passport on spaces and newlines
# - Split every bit on colons
# - Check how many bits from the list are present. ?????
#       Easy. Just pop whatever field was found off the list. list.remove("fieldName")
#       If we have one or more left, check if [0] is cid. If it is, valid.
#       Else, invalid.

# Checking passports with 6 fields or less can speed
# things up, but I won't worry about it for now.

#    Valid fields
#    cid can be ignored
#
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)

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
        if name in checkingFields:
            checkingFields.remove(name)
        else:
            print("Unknown field found: " + name)
            exit(1)
    if len(checkingFields) == 0 or (len(checkingFields) == 1 and checkingFields[0] == 'cid'):
        print("Valid password processed!")
        validCounter = validCounter + 1
    else:
        print("Invalid passport denied!")
        invalidCounter = invalidCounter + 1

print("-----------------------------")
print("Valid: " + str(validCounter))
print("Invalid: " + str(invalidCounter))

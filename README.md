# AdventOfCode2020
This is where my solutions from AoC 2020 go.

#### --- Day 1: Report Repair ---
Simple nested `for` loops. Two loops for part one and three loops for part two.

#### --- Day 2: Password Philosophy ---
First of all, I used some `sed -i 's/://g' day2.input` magic to remove colons. After that it's just working with substrings. I learned about str.count() and used XOR for the first time in Python.

#### --- Day 3: Toboggan Trajectory ---
Quite simple. First I break the map file into rows and then walk through them. If I hit the end of the row, I just double the row and keep going. Do you see the problem with this approach? Me neither :)

#### --- Day 4: Passport Processing ---
For the first part of the assignment I wrote a simple loop that goes through the fields of every passport and removes whatever it finds from the list of required fields. If it reached the end, but there are still fields in the required fields list, passport is marked as invalid and rejected. If not, it is accepted.  
The second part actually makes us check some data, so I wrote a `checkValueValidity` function that I'm not proud of. Pretty sure it can be optimized.

#### --- Day 5: Binary Boarding ---
This one is easy. I replace Fs and Ls with zeros, and Bs and Rs with ones.
The second part is similar, I just had to sort the list and walk through it looking for a missing Seat ID.

#### --- Day 6: Custom Customs ---
Basically it's all about finding unique and common elements. The first one is about removing duplicate characters by converting strings to sets. Part two is about looking for common elements in lists.
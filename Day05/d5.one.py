#!/usr/bin/env python3

# FBFBBFF RLR
# F is 0
# B is 1
# L is 0
# R is 1
# seat ID = row * 8 + column

ticketListFile = "day5.input"
ticketListHandle = open(ticketListFile, 'r')
ticketList = ticketListHandle.readlines()
ticketListHandle.close()

seatIDs = []

for ticket in ticketList:
	ticket = ticket[:-1] # getting rid of newline
	binary = ''
	for char in ticket:
		if char == 'F' or char == 'L':
			binary = binary + '0'
		else:
			binary = binary + '1'
	row = binary[:7] # first 7 characters
	col = binary[7:] # last 3 characters
	row = int(row, 2)
	col = int(col, 2)
	seat = row * 8 + col
	seatIDs.append(seat)

print(max(seatIDs))

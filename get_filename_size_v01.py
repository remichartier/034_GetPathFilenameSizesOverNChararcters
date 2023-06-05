#!/usr/bin/python

with open("test.txt") as file:
    for line in file:
    	if len(line.rstrip()) >= 200:
        	print(line)


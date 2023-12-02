import re

with open("day1\input.txt") as f:
    data = f.read()

def calibration(data):
    
    dataslist = data.split() #makes a list in which each data is a line
    num = [re.findall('\d', lines) for lines in dataslist] #makes a list with lists of numbers in each line
    linesum = (int(n[0] + n[-1]) for n in num) 
    result = sum(linesum)
    return result

#Part 1
print(calibration(data))

#Part 2
data = (
    data.replace('one','o1e')
    .replace('two','t2o')
    .replace('three','t3e')
    .replace('four','f4r')
    .replace('five','f5e')
    .replace('six','s6x')
    .replace('seven','s7n')
    .replace('eight','e8t')
    .replace('nine','n9e')
) #if we replace normally, we could miss numbers, for example 'twone' would become 2ne, and 'one' wouldn't be the last digit of the line anymore
print(calibration(data))
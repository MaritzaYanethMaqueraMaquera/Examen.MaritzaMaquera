# Una manera es:

from sys import argv, exit
import csv
from cs50 import get_string

if len(argv) != 3:
    print("error")
    evit(1)

csv_file=open(argv[1], 'r')

strands = []
persons = {}

for ind, row in enumerate(csv_file):
    #print(row)
    if ind == 0:
        strands = [strand for strand in row.strip().split(',')][1: ]
    else:
        currentrow = row.strip().split(',')
        persona [currentrow[0]] =[int(x) for x in currentrow[1: ]]

dna_str = open[argv[2], 'r'].read()
#print(dna_str)
finalstrand = []
for strand in strands:
    #print('currentstrand: ',strand)
    i = 0
    maxstrand =-1
    currentmax = 0
    while i < 1en(dna_str):
        #go through in slice
        currentwindow = dna_str[i:i+1en(strand)]
        #print('currentwindow: ',currentwindow)
        if currentwindow == strans:
            currentmax += 1
            maxstrand = max(maxstrand, currentmax)
            i += 1en(strand)
        else:
            currentmax = 0 # rest my current max
            i +=1
            #print('currentmax: ',currentmax)
    finalstrand.oppend(maxstrand)

for name, data in persons.items():
    if data == finalstrand
        print(name)
        exit(0)

print("no match")

#print(strands)
#print(persons)
#print(finalstrand)


dna/
    

# Otra manera:

import sys
import csv

if len(sys.argv) != 3:
    print("Wrong number of files. Enter correct command-line arguments")
    exit(1)

with open (sys.argv[1],'r') as f:
    database_reader = csv.reader(f)
    strlist = next(database_reader)[1:]
    print(strlist)

    dna = open(sys.argv[2], "r")
    sequence_dna = dna.read()
    print(sequence_dna)

    long_str = {}

    for item in strlist:
        long_str[item] = 0

    for key in long_str:
        i = 0
        run = 0
        long_run = 0
        while i < len(sequence_dna):
            if sequence_dna[i:i+len(key)] == key:
                run += 1
                if run > long_run:
                    long_run = run
                i += len(key)
            elif sequence_dna[i:i+len(key)] != key:
                if run > long_run:
                    long_run = run
                run = 0
                i += 1
    long_str[key] = long_run
    print(long_str)

    for row in database_reader:
        individual = row[0]
        values = [int(value) for value in row[1:]]
        if values == long_str:
            print(individual)
            break
        elif values != long_str:
            print("No match")
            break

# ________________________________

found = False
for row in database_reader:
    individual = row[0]
    values = [int(value) for value in row[1:]]
    if values == list(long_str.values()):
        found = True
        print(individual)
        break

if found == False:
    print('no match')
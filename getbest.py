#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Idenify the columns that contain the marks and student numbers '''
    ''' Index was not incrememting and starting from an incorrect value'''
    headings = f.readline().strip().split(",")
    i = 0
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
        i += 1
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    ''' Student number was not being recovered'''
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
            best = mark
            best_idx = int(data[num_col])
    return best_idx, best
def data(testF):
    ''' Is used by the Unit test code to open the csv file that contains the data'''
    f = open(testF)
    return f

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f,num_col,mark_col)
    print("The top student was student %s with %d"%(best_idx,best))

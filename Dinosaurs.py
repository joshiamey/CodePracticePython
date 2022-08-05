"""You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information."""
import csv
import math
from queue import PriorityQueue

def get_bipedal_dinos():
    dinodict = {}
    hq = PriorityQueue()
    
    g = 9.8
    with open('./testdata/dataset2.csv', mode='r') as csv_file: #o(n)
        csv_reader = csv.DictReader(csv_file,delimiter=',')
        
        for dicts in csv_reader:
            key1,key2,key3 = dicts.keys()
            dinoname = dicts[key1]
            stridelength = dicts[key2]
            stance = dicts[key3]
            # Only store the dinos with bipedal stance in the dictionary
            if stance == 'bipedal':
                dinodict[dinoname] = float(stridelength)
                
    with open('./testdata/dataset1.csv', mode='r') as csv_file: #O(nlogn)
        csv_reader = csv.DictReader(csv_file,delimiter=',')
        
        for dicts in csv_reader:
            key1,key2,key3 = dicts.keys()
            dinoname = dicts[key1]
            leglenth = float(dicts[key2])
            
            # based on the formula , calculate dinospeed and push it into minheap
            if dinoname in dinodict:
                dinospeed = ((dinodict[dinoname]/leglenth) - 1) * math.sqrt(leglenth * g)
                hq.put((dinospeed,dinoname))

    bipedal_dinos = len(dinodict) * ['']
    
    iter_index = len(bipedal_dinos) - 1
    while not hq.empty(): #O(nlogn)
        bipedal_dinos[iter_index] = hq.get()[1]
        iter_index -= 1
        
    return bipedal_dinos
    
if __name__ == "__main__":
   
    bipedal_dinos = get_bipedal_dinos()
    
    print(bipedal_dinos)
    
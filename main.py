import numpy as np

counter = 0
final = []
with open('input.txt', 'r') as f:
    for line in f:
        values = line.strip().split(',')
        integers = []
        for value in values:
            x, y = map(int, value.split('-'))
            integers.append(x)
            integers.append(y)
        final.append(integers)

def Compare(values):
    
    if values[0] <= values[2] and values[1] >= values[3]:
        global counter
        counter += 1
    elif values[2] <= values[0] and values[3] >=values[1]:
        counter += 1
        
for i in final:
    Compare(i)
    
print (counter)

##part 1 end
overlapCounter = 0

def Overlaps(values):
    if values[0] >= values[2] and values[0] <= values[3]:
        global overlapCounter
        overlapCounter +=1
    elif values[1] >= values[2] and values[1] <= values[3]:
        overlapCounter +=1
        
    elif values[2] >= values[0] and values[2]<= values[1]:
        overlapCounter +=1
    elif values[3] >= values[0] and values[3]<= values[1]:
        overlapCounter +=1

for i in final:
    Overlaps(i)
print(overlapCounter)
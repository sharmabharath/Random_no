from math import floor
from random import shuffle
import numpy as np
from randomtimestamp import randomtimestamp 
import pandas as pd
import csv

# randomtimestamp(2021).split()[1]
# numbers = []
# approx_num = []
time = []
numbers_integer = []
rangeHolder = []
sum1 = 0

#inputs
max_range = 40
wing = 20
total_customers = 500

def more_than_range(numbers):
    for i in range (0, len(numbers)):
        # numbers.sort()
        if(numbers[i] > max_range):
            rangeHolder.append(numbers[i]-max_range)
            numbers[i] = max_range
    length_rangeHolder = len(rangeHolder)
    if((length_rangeHolder )!= 0):
        average_rangeHolder = sum(rangeHolder)/len(rangeHolder)
    else:
        return numbers
    for i in range (0, len(rangeHolder)):
        if(numbers[i]== min(numbers)):
         numbers[i] = average_rangeHolder + numbers[i]
    # numbers.sort()

    for i in range (0, len(numbers)):
        if (numbers[i] > max_range):
            more_than_range(numbers)
        else:
            return numbers

    # return numbers 
#GETTING FLOAT VALUES AND COVERTING TO INT VALUES LESS THAN TOTAL_NO_CUSTOMERS
def generateRandomNumbers():

    # numbers.append(np.random.dirichlet(np.ones(10)) * 100)
    temp = np.random.dirichlet(np.ones(wing) ) * total_customers
    numbers = np.floor(temp).astype(int)
    print("numbers are", numbers)
    print("temp here is",temp)


# np nd.array convert python int
    for i in numbers: 
        temp1 = np.int16(i).item()
        numbers_integer.append(temp1)
    print("NUMBER INTEGER 1",numbers_integer)
# print(numbers_integer)
    sum1 = sum(numbers_integer)
    less_than_100 = total_customers - sum1
    numbers_integer[0] += less_than_100
# sum1 = sum(numbers_integer)
    print("NUMBER INTEGER 2", numbers_integer)
    # numbers_integer.sort()
    print("NUMBER INTEGER 3", numbers_integer)
    more_than_range(numbers_integer)
    print("NUMBER INTEGER 4", numbers_integer)

generateRandomNumbers()
print(numbers_integer)
details = []
for i in range (0, len(numbers_integer)):
    wings = []
    wings.append(i+1)
    print(f"wings here is {wings}")
    wings.append(numbers_integer[i])
    print(f"wings here is 2 {wings}")

    details.append(wings)


print(f"\n\n[wings, number of cars] is \n\n {details}")
# print(f"Range is : {details[1][1]}")
print(time)
    
#random time generator
# for i in range (0, 3):
#     temp = randomtimestamp(2021).split()[1]
#     time.append(temp)

# details[0].append(time for i in range (0, details[i][1]))
print(f"length is {len(details)}")

for i in range (0, len(details)):
    time = []
    for j in range (0, int(details[i][1])):    
        temp = randomtimestamp(2021).split()[1]
        time.append(temp)
    details[i].extend(time)


fields = ['wings', 'cars', 'time']
rows = details
 
with open(f'GFGNOT.csv', 'w') as f: 
      
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
    write.writerow(fields) 
    write.writerows(rows) 




print(f"\n\n with time : {details}")

# export to csv file
fields = ['wings', 'cars', 'time']
shuffle(details)
rows= details

with open(f'GFGSHUFFLED.csv', 'w') as f: 
      
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
    write.writerow(fields) 
    write.writerows(rows)

 
 




# [
#     "1:[12]:[TIME]:BASEMENT",
#     "2:[22]:[TIME]:BASEMENT",
#     "3:[14]:[TIME]:BASEMENT",
#     "4:[12]:[TIME]:BASEMENT",
#     "5:[10]:[TIME]:BASEMENT",
#     "6:[22]:[TIME]:BASEMENT",

# ]
 


# desired output    BASEMENT --- > WINGS ----> CARS -----> TIME

#BASEMENT 
# basement = [b1,b2,b3]
# wing = [w1, w2, w3, ]
# wing_Car = [[1, 0, 0 ,0 ,1],[1,0,0,1,0,1], [1,0,0,1,0,0,1]]
# time = [ [1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1]]
# details(b1[0], wing[0], wing_Car[0], time[0])


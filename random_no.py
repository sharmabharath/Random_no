from math import floor
import numpy as np

# numbers = []
# approx_num = []
numbers_integer = []
rangeHolder = []
sum1 = 0

#inputs
max_range = 50
wing = 20
total_customers = 500

def more_than_range(numbers):
    for i in range (0, len(numbers)):
        numbers.sort()
        if(numbers[i] > max_range):
            rangeHolder.append(numbers[i]-max_range)
            numbers[i] = max_range
    length_rangeHolder = len(rangeHolder)
    if((length_rangeHolder )!= 0):
        average_rangeHolder = sum(rangeHolder)/len(rangeHolder)
    else:
        return numbers
    for i in range (0, len(rangeHolder)):
        numbers[i] = average_rangeHolder + numbers[i]
    numbers.sort()

    for i in range (0, len(numbers)):
        if (numbers[i] > max_range):
            more_than_range(numbers)
        else:
            return numbers

    # return numbers 

def generateRandomNumbers():

    # numbers.append(np.random.dirichlet(np.ones(10)) * 100)
    temp = np.random.dirichlet(np.ones(wing) ) * total_customers
    numbers = np.floor(temp).astype(int)
    print(type(numbers))


# np nd.array convert python int
    for i in numbers: 
        temp1 = np.int16(i).item()
        numbers_integer.append(temp1)

# print(numbers_integer)
    sum1 = sum(numbers_integer)
    less_than_100 = total_customers - sum1
    numbers_integer[0] += less_than_100
# sum1 = sum(numbers_integer)
    numbers_integer.sort()
    more_than_range(numbers_integer)

generateRandomNumbers()
print(numbers_integer)
details = []
for i in range (0, len(numbers_integer)):
    wings = []
    wings.append(i+1)
    wings.append(numbers_integer[i])

    details.append(wings)

print(f"\n\n[wings, number of cars] is \n\n {details}")

    
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

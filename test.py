from math import floor
from random import shuffle
import numpy as np
from randomtimestamp import randomtimestamp
import pandas as pd
import csv

#value initialization
time = []
numbers_integer = []
rangeHolder = []
sum1 = 0
carsArray=[]
#inputs
max_range = 40
wings = 20
total_customers = 500
s = 0.9
 
def more_than_range(cars):
 
    for i in range(0,len(cars)):
        if(cars[i]>max_range):
            print("here")
            rangeHolder.append(cars[i]-max_range)
            cars[i]= max_range
        if(len(rangeHolder)!=0):
            averageRange = sum(rangeHolder)/len(rangeHolder)
        else:
            return cars
        for i in range(0,len(rangeHolder)):
            if(cars[i]== min(cars)):
                cars[i] = cars[i]+averageRange
  
  


def generateRandomNumbers():
    cars = np.random.multinomial(total_customers, np.random.dirichlet(np.ones(wings) * s))
  
    for i in cars:
        temp1 = np.int16(i).item()
        carsArray.append(temp1)

    print(carsArray, sum(carsArray))
    more_than_range(carsArray)
       
generateRandomNumbers()


 





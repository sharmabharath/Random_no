import numpy as np

time = []
numbers_integer = []
rangeHolder = []
sum1 = 0

#inputs
max_range = 50
wing = 20
total_customers = 500

temp = np.random.dirichlet(np.ones(wing) ) * total_customers
print(sum(temp))
print(temp)

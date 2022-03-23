#high_low.py
"""Create a tuple representing day of the week (string) and high,low,high
temperatures(integers). Display the tuple.
a) Use the [] operator to access all elements of the touple.
Unpack the touple to the list of coma separate variables, day, low, hig."""

high_low = ('Monday',23,12)
print(f'high_low={high_low}')

#access to all elements of the tuple
print(f'high_low[0]:{high_low[0]} high_low[1]={high_low[1]} high_low[2]={high_low[2]}')

#unpack the the touple
# day, high = high_low  - ValueError, because one variable is missing on left side (sequence list of variables)
day, high, low = high_low
print(f'day:{day} high:{high} low:{low}')
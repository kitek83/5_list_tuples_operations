#reversed_zip_functions.py
"""
Showing operation of built in functions: reversed() zip(),pd.Series(), pd.DataFrame.
"""
import pandas as pd
# 1.reversed() returns the iterator, which enables you to itrerate over sequence's values backward.
# The following list comprehension creates a new list containing the square's of numbers' values
# in reverse order:
numbers = [10,3,7,1,9,4,2,8,5,6]
reverse_numbers = [num**2 for num in reversed(numbers)]
print(f'numbers={numbers}')
print(f'reverse_numbers={reverse_numbers}')

print(f'numbers={numbers}')
numbers.sort()
print(numbers)
print()

# 2.zip() - enables you to iterate over multiple iterables of data at the same time.
#   zip() - creates the tuple at the same index in each. Then we have to unpack the tuple.
names = ['Jack','Kris','Amanda','John','Koko','Kamil']
grades = [3.5,6.3,5,4.3,56,90]

for nam, grad in zip(names,grades):
    print(f'name={nam}; Grade={grad}')

"""
out:
name=Jack; Grade=3.5
name=Kris; Grade=6.3
name=Amanda; Grade=5
name=John; Grade=4.3
name=Koko; Grade=56
name=Kamil; Grade=90
"""
print()
#Try to use pandas Series to atchieve above result
ps_series = pd.Series([grades, names])
print(f'ps_series:\n{ps_series}')
"""
out:
ps_series:
0                 [3.5, 6.3, 5, 4.3, 56, 90]
1    [Jack, Kris, Amanda, John, Koko, Kamil]
dtype: object
"""
#try to use pd.DataFrame
pd_DataFrame = pd.DataFrame(grades,names) #this is similar to zip()
print(f'pd_DataFrame=\n{pd_DataFrame}')
"""
out:
pd_DataFrame=
           0
Jack     3.5
Kris     6.3
Amanda   5.0
John     4.3
Koko    56.0
Kamil   90.0
"""
print()
#try to use keyword= index with pd.DataFrame
pd_DataFrame2 = pd.DataFrame(grades, index=names) #the same like above
print(f'pd_DataFrame2={pd_DataFrame2}')



















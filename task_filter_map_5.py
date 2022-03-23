# task_filter_map_5.py
"""
task1
Crete a list called numbers containing 1 through 15, then perform following tasks:
a) Use built in function filter with lambda to select only number's even elements.
b) Use built in function map with lambda to square values of number's elements.
c) Filter number's even elements, then map them to their squares.
"""
numbers = list(range(1,16)) #list iterate throug range object
print(f'numbers={numbers}')
#out: numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#a)filter() - works with conditions
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f'even={even}')

#b)map() - works with simple expressions
squared = list(map(lambda x: x**2, numbers))
print(f'squared={squared}')

#c)
even_suared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f'even_suared={even_suared}') #list iterate through lazy function map()
print()
"""
Map a list of the 3 Farenheit temperatures 41,32,212 to a list of tuples containing 
the Farenheit temperatures and their Celcius eqivalents.
Celsius = (Farenheit - 32) * (5/9)
"""
temp_f = [41,32,212]
tups_f_c = list(map(lambda x: (x,(x-32)*(5/9)), temp_f)) #lambda's expression (x,(x-32)*(5/9)) creates tuple
print(f'temp_f={temp_f}')
print(f'tups_f_c={tups_f_c}')
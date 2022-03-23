# del_sequence
"""del statement can be used to remove elements from the list."""
number = range(0,10)
print(f'number = range(0,10)=>{number}') #alone range is not working

numbers = list(range(10))   #range works with the list, where list is hogher ordered function
print(f'numbers={numbers}')

#delete last elelement
del numbers[-1]
print(f'numbers={numbers}')

#delete first 2 elements
del numbers[0:2]
print(f'numbers={numbers}')

#use step2 to delete every other element
del numbers[::2]
print(f'numbers={numbers}')

#delete all of the list's elements
del numbers[:]
print(f'numbers={numbers}')
# sequence_slicing.py
"""Slice sequences operations."""
#slice with start and ending indices
numbers = [2,3,5,7,11,13,17,19]
print(f'numbers[2:6]={numbers[2:6]}')
print(f'numbers[:6]={numbers[:6]}')
print(f'numbers[6:]={numbers[6:]}')
print(f'numbers[6:len(numbers)]={numbers[6:len(numbers)]}')

#copies the entire sequence
print(f'numbers[:]={numbers[:]}')

#last element from the list
print(f'numbers[-1]={numbers[-1]}')

#slicing with steps - shows every 2nd element of the sequence
print(f'numbers[::2]={numbers[::2]}') #copy the slice of the elements, but list is unchanged

#list in reverse order
print(f'numbers[::-1]={numbers[::-1]}')   #reverse the list and list is changed now
print(f'{numbers.sort(reverse=True)}')   #out: None
print(f'numbers={numbers}')

print(f'numbers[::-1]={numbers[::-1]}')         #come back to previous order
print(f'numbers[-1:-9:-1]={numbers[-1:-9:-1]}')
print()

#modifying lists via slices
numbers = [2,3,5,7,11,13,17,19]
numbers[0:3] = ['two','three','five']
print(f"numbers[0:3] = ['two','three','five']={numbers}")
print()

#delete only the first 3 elements of the list numbers
numbers[0:3] = []
print(f'numbers[0:3] = [] = {numbers}')
numbers = [2,3,5,7,11,13,17,19]

#assign lists elens to a slice with step 2
numbers[::2] = [100,100,100,100]  #must assigne sequenze of 4 because extended slise is size 4
print(f'numbers[::2] = [100,100,100,100]=>{numbers}')

#delete all elements of the sequence
numbers[:] = []
print(f'numbers[:] = [] => {numbers}')
print(f'id(numbers)={id(numbers)}')
print()
numbers = [2,3,5,7,11,13,17,19]
print(f'{numbers}')
#assigning numbers a new empty list
numbers = []
print(f'numbers = []:{numbers}')
print(f'id(numbers)={id(numbers)}')























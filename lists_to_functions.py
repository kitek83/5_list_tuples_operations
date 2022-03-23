#lists_to_functions.py
"""Passing entire lists to function.
Consider the function modify_elements, which receives a reference to a list 
and multiples each of the list's element values by 2."""

#solution1
def modify_elements(reference):
    return [x*2 for x in reference]

numbers = [10,3,7,1,9]
print(f'numbers={modify_elements(numbers)}')
print(f'numbers={numbers}')
print()

#solution2 - changing permanently list numbers
def modify_elements2(values):
    for num in range(len(values)):
        values[num] *= 2

print(f'numbers={numbers}')
modify_elements2(numbers)
print(f'modified_numbers={numbers}')

#passing tuple will cause an exception TypeError: 'tuple' object does not support item assignment
# tuple1 = (2,3,4,5)
# modify_elements2(tuple1)


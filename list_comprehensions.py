#list_comprehensions.py
"""Script showing functional-style features with list comprehensions - a concise
and convenient notation for creating new lists."""

#list comprehensions can replase many for statements that iterate over existing sequences
#and create new lists, such as
list1 = []
for i in range(1,6):
    list1.append(i)
print(f'list1={list1}')

#using the list comprehension to create the same list of integers
list2 = [x for x in range(1,6)]
print(f'list2={list2}')
list3 = [x for x in range(1,8)]
print(list3)

#list2 cam be expressed more concisely using the function list
list4 = list(range(1,6))
print(f'list4={list4}')
print()

"""list comprehension expression can perform tasks such as calculations, that map elements to a new values 
    (possible of different type).The following comprehension maps each value to its cubes with the expressions
    item**3"""
cubes = [item**3 for item in range(1,6)]
print(f'cubes={cubes}')
print()

#using if clause with list comprehension produces  a list with fewer elements than the data being filtered
#The following included in list4 only even values produced by the for clause:
list4 = [item for item in range(1,11) if item % 2 == 0]
print(f'list4={list4}')

#List comprehension that process another list elements.
"""The for clause can process any iterable. Let's create a list of lowercase strings
   and use list comprehension to produce a new list containing their uppercase version"""
colors = ['red','orange','yellow','green','blue']
uppercase = [color.upper() for color in colors]  #list comprehension with expresion and for clause created new list
print(f'uppercase={uppercase}')
print(f'colors={colors}')
title = [color.title() for color in colors]
print(f'title={title}')


























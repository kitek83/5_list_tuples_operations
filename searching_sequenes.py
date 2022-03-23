#searching_sequenes.py
"""Ussing method index() to determine whether a sequence (such as list,tuple,string)
contains a value htat metches particular key value"""

numbers = [3,7,1,4,2,8,5,6]
print(f'numbers.index(5)={numbers.index(5)}')  #takes the argument a search key and returns index nr

#use *= to multiply the sequence
numbers *= 2        #creats 2nd the same list
print(f'numbers={numbers}')
#out: numbers=[3, 7, 1, 4, 2, 8, 5, 6, 3, 7, 1, 4, 2, 8, 5, 6]

#searches for value=5 from index nr 7
print(f'numbers.index(5,7)={numbers.index(5,7)}')

#specyfying the ending index to search
print(f'numbers.index(7,0,3)={numbers.index(7,0,3)}')

#searching the string's index
names = ['Jack','Kris', 'Amanda', 'John']
print(f"names.index('Kris')={names.index('Kris')}")

#usingg operator 'in' to check if the right operand-iterable contains ledt operand-value
print(f'100 in numbers={100 in numbers}')
print(f'7 in numbers={7 in numbers}')

#similarly isomg operator 'not in'
print(f'100 not in numbers={100 not in numbers}')
print()

#using operator 'in' to prevent ValueError
key = 7
if key in numbers:
    print(f"key={key} is in numbers and it's index is {numbers.index(key)}")
else:
    print(f'key={key} is not in numbers')



























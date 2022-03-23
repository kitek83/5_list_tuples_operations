#filter_map_reduce.py
"""
In the script I will demonstrate the built-in filter and map functions
for filtering and mapping respectively. Then I will show reductions in which
I will process the collection of elements into single value.
"""
#1.Usin filter():
"""
Let's use built-in function filter() to obtain the odd values in numbers:
"""
numbers = [10,3,7,1,9,4,2,8,5,6]

def is_odd(x):
    #returns true only if x is odd:
    return x % 2 != 0

#filter() return values, which are odd. filter() works with the functions, which return True/False and it doesn't work with the simple expressions
filtered = list(filter(is_odd, numbers)) #filter() - higher ordered function call is_odd for each element of the  list numbers

print(f'filtered={filtered}') #filter() returns iterator od odd numbers and function list() must iterate through it to get filtered results

#map() return boolean values True/False for condition x % 2 != 0
mapped = list(map(is_odd, numbers))
print(f'mapped={mapped}')

#map() with lamba function
mapped2 = list(map(lambda x: x % 2 != 0, numbers)) # if it's used condition operator !=, ==..map() returns True/False
print(f'mapped2={mapped2}')
#out: mapped2=[False, True, True, True, True, False, False, False, True, False]
print()

#Using map() with simple expression. map() returns maped values for the funxtions, which returs simple expressions
#map() return True/ False for the functions, which return conditions like ==, !=
mapped3 = list(map(lambda x: x**2, numbers)) #in this way map() returns squared values of the sequence numbers
print(f'mapped3={mapped3}')
#out: mapped3=[100, 9, 49, 1, 81, 16, 4, 64, 25, 36]

#the same result for above using list comprehension
mapped3_compr = [x**2 for x in numbers]
print(f'mapped3_compr={mapped3_compr}')

#Let's use filter() for the above to see diference compared map()
filtered2 = list(filter(lambda x: x**2, numbers)) #filter() doesn't work with simple expressions, only works with conditions
print(f'filtered2={filtered2}')
#out: filtered2=[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print()
#The same rsult as above filter() with using list comprehension with if clause
#1st solution:
l_compr = [val for val in numbers if val % 2 != 0]
print(f'l_compr={l_compr}')

#2nd solution:
l_compr2 = [num for num in numbers if is_odd(num)] #new - looks like, that in list compr. is_odd(x) returns condition= x % 2 != 0
print(f'l_compr2={l_compr2}')
print()

#using lambda function (expression) or simply lambda
#lambda parameter: expression
result1 = (lambda x: x + 1)(5)
print(f'result1={result1}')

result2 = (lambda x,y,z: x**2/342 + x**6/21322 - z**0.6)(23.45,45.67,98.32)
print(f'{"result2":>16}={result2:>10.3f}') #here f'string() with format specifiers :>.f
print()

#combining filte() and map() to get squared values of  odd numbers from the numbers list
print(f'numbers={numbers}')
#conditions -> filter(), expressions -> map()
filt_map = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0,numbers)))
print(f'filt_map={filt_map}')
#out: filt_map=[9, 49, 1, 81, 25]
#lambda() and filter() are the lazy functionsm and they return the values when the lis() iterate through them

#using list comprehension to the preceding snippet
list_filt_map = [x**2 for x in numbers if x % 2 != 0]
print(f'list_filt_map={list_filt_map}')
#For each value of x in numbers, the expression x**2 is performed only if the condition x % 2 != 0 is True




























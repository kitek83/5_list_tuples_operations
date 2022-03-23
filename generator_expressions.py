#generator_expressions.py
"""Generator expressions are similar to the  list comprehension, but creates iterable
   generator objects that produces values on demand."""
#the generator expression squares and return only the odd values in numbers:
numbers = [10,3,7,1,9,4,2,8,5,6]

#generator expressio we define with parentheses
for i in (x**2 for x in numbers if x % 2 != 0):
    print(i, end=' ')

#to show that generator expression does not create the list
square_of_odds = (x**2 for x in numbers if x % 2 != 0)
print(f'\nsquare_of_odds={square_of_odds}')
#out: square_of_odds=<generator object <genexpr> at 0x000001FF12395C80> -> indicates, that
#square_of_odds is generator object that was created from generator expression <genexpr>

for x in square_of_odds:   #generator object produces values on demand
    print(x, end=' ')
#out: 9 49 1 81 25

"""
Task1
Create a generator expression that cubes the even integers in a list 
containing 10,3,7,1,9,4,2. Use function list to create list of the 
results. Note that function's parentheses also act as generator expression parentheses.
"""
numbers = [10,3,7,1,9,4,2]
cubes = list(num**3 for num in numbers if num % 2 == 0)
print(f'cubes={cubes}')



























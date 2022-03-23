#list_task4.py
"""Task1.Use a list comprehension to create list of tuples containing the numbers 1-5 and their cubes-
   that is, [(1,1),(2,8),(3,27),...]"""
tuple_list = [(x,x**3) for x in range(1,6)]  #-->new for me
print(f'tuple_list={tuple_list}')
#out: tuple_list=[(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

"""Task2.Use a list comprehension and range function with a step to create a list 
   with multiples of 3 that are less than 30"""
#answer:
multiples = [x for x in range(3,30,3)]
print(f'multiples={multiples}')
#out: multiples=[3, 6, 9, 12, 15, 18, 21, 24, 27]
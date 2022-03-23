#primitive_bar_chart.py
"""Creates a primitive bar charrt, where bar's length is made of astericks(*) and
is proportional to the list's corresponding element value"""
numbers = [19,3,15,7,11]

print('Creating a bar chart from numbers:')
print(f"Index{'Value':>8}   Bar")   #using function's f'string' format  specifier :>8 - right aligned, field nr 8

#using function enumerate() to access to the list's indices and values safely
for index, value in enumerate(numbers):
    print(f"{index}{value:>12}   {'*'*value}")

"""output:
Creating a bar chart from numbers:
Index   Value   Bar
0          19   *******************
1           3   ***
2          15   ***************
3           7   *******
4          11   ***********

"""
#list_reminder_1.py
"""List operations without descriptions. This is only reminder."""
#1. list() + enumerate()
colors = ['red','black', 'yellow']
colors_en  = list(enumerate(colors))
print(f'colors_en={colors_en}')
#out: colors_en=[(0, 'red'), (1, 'black'), (2, 'yellow')]

#2. Generator expression.
numbers = [1,2,3,4,5,6,7,8,9,12,23,44,55]

for value in (x**2 for x in numbers if x % 2 != 0):
    print(value,end=' ')

#3.filter() and map()
filter_map = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f'\nfilter_map={filter_map}')

#4.list -map -(farenheit, celsius)
farenheit = [41,32,212]
far_cel = list(map(lambda x: (x, (x-32)*(5/9)),farenheit))
print(f'far_cel={far_cel}')
#out: far_cel=[(41, 5.0), (32, 0.0), (212, 100.0)]
print()

#5. zip()
names = ['Amanda','John','Kris']
surnames = ['Koko','Mencel','Kozak']
grades = [6.7,8,10]

for grade,name,surname in zip(grades, names, surnames):  #unpack iterator containing tuples
    print(f'grade={grade}-->name:{name}, surname:{surname}')
"""
out:
grade=6.7-->name:Amanda, surname:Koko
grade=8-->name:John, surname:Mencel
grade=10-->name:Kris, surname:Kozak
------------------------------------
zip() receives as an argument any number of iterables and returns an iterator that produces tuples
containing the elements at the same index in each.
"""
#for check
print(list(zip(grades,names,surnames)))
#out: [(6.7, 'Amanda', 'Koko'), (8, 'John', 'Mencel'), (10, 'Kris', 'Kozak')]
#zip() produces the tuples as above, consisting of the elements at index 0,1,2 of each list.

#6.zip() adds corresponding indices from 2 lists
lists_sum_zip = [(a+b) for a,b in zip([10,20,30],[1,2,3])]
print(f'lists_sum_zip={lists_sum_zip}')























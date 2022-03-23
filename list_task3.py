#list_task3
"""Create a list called numbers containing the values from 1 to 15,
then use del statement to perform the following operations consecutively:
a)Delete a slice containing the first four elements and show the resulting list
b)Starting with the first element use the slice to delete every other element of the list,
then show the resulting list."""

numbers = list(range(1,16))
#out: numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'numbers={numbers}')

#a)
del numbers[0:4]            #numbers sequence is now permanently changed
print(f'numbers={numbers}')
print(f'numbers={numbers}')

#b)
del numbers[::2]
print(f'numbers={numbers}')
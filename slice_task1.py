#slice_task1.py
"""Create a list called numbers containing the values from 1 to 15, then use slices to perform the
following operations consecutively:
a) Select number's even integers.
b) Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
c) Keep only the first five elements, then show the resulting list.
d) Delete all the remaining elements by assigning to a slice. Show the resulting list."""

numbers = [x for x in range(1,16)] #using comprehension list
"""out
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]"""
print(f'numbers={numbers}')

#a) must use the slices to select number's even integers
print(f'odd_numbers=numbers[::2]=>{numbers[::2]}') #operation does't change original numbers sequence
print(numbers)
print(f'{numbers[::3]}')
print(f'{numbers[14]}')
print(len(numbers))

#use the slices to select number's even integers
print(f'even_integers=numbers[1:len(numbers):2]=>{numbers[1:len(numbers):2]}') #3rd variable in the slice=2 is the step
print()

#b)
numbers[5:10] = [0,0,0,0]  #changing original list
print(f'numbers[5:10] = [0,0,0,0]=>{numbers}')
print(numbers)

#c) #1st solution
numbers[5:len(numbers)] = []
print(f'numbers[5:len(numbers)] = []=>{numbers}')

#2nd solution
numbers = [1, 2, 3, 4, 5, 0, 0, 0, 0, 11, 12, 13, 14, 15]
print(numbers)
numbers[5:] = []
print(f'numbers[5:] = []=>{numbers}')

#d)
numbers[:] = []
print(f'numbers[:] = []=>{numbers}')




























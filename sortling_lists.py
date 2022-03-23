#sortling_lists.py
"""Sorting enables you to arrange data either in ascending or descending order."""

numbers = [10,3,7,1,9,4,2,8,5,6]
numbers2 = [10,3,7,1,9,4,2,8,5,6]
print(f'numbers={numbers}')

numbers.sort()                  #List's method .sort() - modifies the list in ascending order
print(f'sorted_numbers={numbers}')

#list in descending order
descending_order = numbers.sort(reverse=True)   #.sort is not working with assigned variable descending_order, because it refers to the var numbers
print(f'descending_order={descending_order}')

numbers.sort(reverse=True)
print(f'numbers.sort(reverse=True)=>{numbers}')

print()
print(f'numbers2={numbers2}')
print(f'sorted(numbers2)={sorted(numbers2)}')   #Function sorted() return a new list
print(f'numbers2={numbers2}')
print()

letters = 'ffefewofiqrriw'
ascendin_letters = sorted(letters) #sorted() creats the list
print(f'letters={letters}')
print(f'ascendin_letters={ascendin_letters}')
print()

letters2 = []
letters2 += 'ffefewofiqrriw'   #creating the list from the string via augmented assignment
print(f'letters2={letters2}')
letters2.sort(reverse=True)     #using reverse keyword argument (of the list's .sort()method) set to True
print(f'letters2_reversed={letters2}')

#you can sor any sequence (immutable, mmutable) withour modifying it by using built in function sorte()
#which returns a new list containing the sorted elements of its argument sequence
print()
letters3 = 'tttoorroewaaddbbewfra'
print(f'letters3={letters3}')
sorted_letters3 = sorted(letters3)   #returns new sorted list
print(f'sorted_letters3={sorted_letters3}')
print(f'letters3={letters3}')

#task
"""Create food list containing 'Cookies', 'pizza','Grapes','apples','steak', 'Bacon'
Use list method .sort() to sort the list in ascending order. Are the strings in alphabetical order?"""

food = ['Cookies', 'pizza','Grapes','apples','steak', 'Bacon']
food.sort()
print(f'food:{food}')  #printed in lexicographical order - upper case letters values are lower the lowercase  letter values




















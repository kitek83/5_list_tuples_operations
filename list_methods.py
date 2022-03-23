# list_methods.py
"""Other list's methods: insert(), append(), extend(), remove(), clear(), count(),
reverse(), copy()"""

#method insert - adds new intem at a specified index
colors = ['orange','yellow','green']
print(f'colors={colors}')
colors.insert(0,'red')
print(colors)

#method append() - add new item at the end of the list
colors.append('blue')
print(colors)

#extend() - add all elements of another sequence at the end of the list
colors.extend(['indigo','violet'])      #this is equivalent of using +=
print(colors)
colors += ['black','yellow']
print(colors)

#adds all emelents of the string and the tuple
sample_list_extend = []
s = 'abc'
sample_list_extend.extend(s)  #automaticallu changes string to the list
print(f'{sample_list_extend}')
sample_list_extend.extend((1,2,3))  #extra parentheses, extend() take only 1 iterable argument
print(sample_list_extend)

for i in s:  #string is iterable
    print(i)

#remove deletes the first element with the specified value
colors.insert(3,'black')
print(colors)
#colors= ['red', 'orange', 'yellow', 'black', 'green', 'blue', 'indigo', 'violet', 'black', 'yellow']
colors.remove('black') #removed 1st 'black'
print(colors)

#copy() - returns a new list containg a shallow copy of the original list
colors2 = colors.copy()  #
colors3 = colors.copy()
print(f'colors2={colors2}')
#equivalent to copy() is a slice operation:
colors_copied = colors[:]
print(f'colors_copied={colors_copied}')
#out: colors_copied=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'yellow']

#clear() deletes all elements from the list
colors.clear()
print(f'colors={colors}')

#clear() is eqivalent to:
colors2[:] = []
print(f'colors2={colors2}')
print()

#count() counting number of occurance of an item
#count() searches for  its arguement and returns the number of times it is found
results = [1,2,5,4,3,5,2,1,3,3,
           1,4,3,3,3,2,3,3,2,2]
print(f'results={results}')
for i in range(1,6):
    print(f'{i} appears {results.count(i)} in results.')

"""out:
1 appears 3 in results.
2 appears 5 in results.
3 appears 8 in results.
4 appears 2 in results.
5 appears 2 in results.
"""

#reverse() - reverses the contents of a lists, rather than creating a reversed copy
print(f'colors3={colors3}')
colors3=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'yellow']
colors3.reverse()
print(f'colors3={colors3}')
print(colors3)
print()

#Task1. Determine the index of 'violet', the use it to insert 'red' before 'violet'
rainbow = ['green','orange','violet']
print(f'rainbow.index("violet")={rainbow.index("violet")}')
rainbow.insert(rainbow.index('violet'),'red') #using highrt ordered function style
print(f'rainbow={rainbow}')

#pop() with no arguements removes and returns the item at the end of the list
"""simulate stacks with lists. Let's create the empty list called stack, push(append) 2 strings
onto it, then pop() the strings to confirm  they are retrieved in last in, first out (LIFO) order."""
stack = []
stack.append('red')
print(f'stack={stack}')
stack.append('green')
print(f'stack={stack}')

#last in is returned and removed
print(f'stack.pop()={stack.pop()}')
print(f'stack={stack}')

#first out is returne and removed
first_out = stack.pop()
print(f'first_out={first_out}')
print(f'stack={stack}')






















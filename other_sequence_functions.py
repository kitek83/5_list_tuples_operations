#other_sequence_functions.py
"""
Showing another sequence processing functions.
"""
from statistics import mean

#1.Reductions -process a sequence elements into a single value.
#sum()
numbers = [22,3,4,55,6,7,3,12]
print(f'sum(numbers)={sum(numbers)}')
print(f'min(numbers)={min(numbers)}')
print(f'max(numbers)={max(numbers)}')
print(f'numbers.count(3)={numbers.count(3)}')
print(f'mean(numbers)={mean(numbers):.2f}')  #mean() imported from statistics

average = sum(numbers) / len(numbers) #reduction funcrions
print(f'average={average:.2f}')
print()

#2. min(), max() - reduction funnctions as keyword argument functions:
print(f"'RED'<'red':{'RED'<'red'}")
#string are compared by their numerical values. Lowercase letter have highrt numerical value then uppercase

#ord() - showinig numerical value of the letter
print(f"ord('R')={ord('R')}")
print(f"ord('r')={ord('r')}")
print()

#consider list colors of the uppercase and lowercase strings and try to arrange them in alphabethical order
colors = ['Red','orange','Yellow','green','Blue','black']
colors2 = colors.copy() #it's not  new list, it's shallow copy of colors list, so if colors list is changed, colors2 list is changed too

colors3 = []
colors3 = colors[:] #it's not a new list. It's shallow copy of colors

colors4 = []
colors4 += colors[:]
colors5 = ['Red','orange','Yellow','green','Blue'] #it's new list
colors6 = [i.lower() for i in colors]
print(colors)
colors.sort() #changin permanently the order of color;s strings
print(f'colors.sort():{colors}')  #sorted in mumerical (lexicographical order)
#out: colors.sort():['Red', 'Yellow', 'blue', 'green', 'orange']
print(colors)
print()

#creating alphabetical order of colors -> you must make all strings uppercase or lowercase
#changing all strings on uppercase
uppercase = [i.upper() for i in colors]
print(f'uppercase={uppercase}')
#out: uppercase=['RED', 'YELLOW', 'BLUE', 'GREEN', 'ORANGE']

uppercase.sort()
print(f'alphabetical_order1={uppercase}')

alphabetical2 = []
alphabetical2 = uppercase[:]  #copy uppercase
print(f'alphabetical2={alphabetical2}')
print()

#The following snippets  enable min() and max() to determin min and max strings alphabetically
print(f'colors2={colors2}')
#out: colors2=['Red', 'orange', 'Yellow', 'green', 'blue']
print(f'colors3={colors3}')
print(f'colors4={colors4}')
print(f'colors5={colors5}')
print(f'colors6={colors6}')
print()

#using min(), max() with key keyword argument which must be one parameter function, thet returns a value
min1 = min(colors2, key=lambda i: i.upper()) #min for alphabetical order
max1 = max(colors2, key=lambda i: i.upper()) #max for alphabetical order
print(f'min1={min1}')
print(f'max1={max1}')
# min() and max() call the key arguemnt's function for each element of the colors2
# and use the results returned by the function to cmpare elements.
print(colors) #for check































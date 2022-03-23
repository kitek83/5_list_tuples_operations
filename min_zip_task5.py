# min_zip_task5.py
"""
Task5.
Create the list foods containing 'Cookies','pizza','Grapes','apples','steak','Bacon'.
Find the smallest string with min(), then reimplement the min() call using the key function to
to ignore the string's case.
"""
foods = ['Cookies','pizza','Grapes','apples','steak','Bacon']

#smallest string with min() acc to numerical values of strings
min_foods_num = min(foods)
print(f'min_foods_numerical={min_foods_num}')

#smallest string ignoring strings' case using alphabetical order
min_foods = min(foods, key=lambda i: i.lower())
print(f'min_foods_alphabetical={min_foods}')
"""
out:
min_foods_num=Bacon
min_foods=apples
"""

print()
#try to count total value in the strin 'apple'
sum1=0
for i in 'apples':
    sum1 += ord(i)

print(f'sum1=sum_apples={sum1}')
print(ord('a'))
print(ord('p'))

#make list foods lowercase
foods2 = [i.lower() for i in foods]
print(f'foods2={foods2}')
#out: foods2=['cookies', 'pizza', 'grapes', 'apples', 'steak', 'bacon']

#try to calculate each string total value from the sequence list2
for word in foods2:
    total = 0
    for i in word:
        total += ord(i)
    print(f"for word:'{word}' --> total value is:{total}")
"""
out:
foods2=['cookies', 'pizza', 'grapes', 'apples', 'steak', 'bacon']
for word:'cookies' --> total value is:749
for word:'pizza' --> total value is:558
for word:'grapes' --> total value is:642
for word:'apples' --> total value is:645
for word:'steak' --> total value is:536
for word:'bacon' --> total value is:515
"""

"""
Task6
Use zip() with 2 integers lists to crete a new list containing the sum of elements
from corresponding indices in both lists.
"""
print()
#list comprehension where for cluse iterate through 2 collections and returns expression (a+b)
new_list  = [(a+b) for a,b in zip([10,20,30],[1,2,3])]
print(f'new_list={new_list}')

#let's make 3 lists as a above but use multiplication expression. zip() allow for stat. to iterate through multiple sequences
new_list2 = [(a*b*c) for a,b,c in zip([10,20,30],[1,2,3],[5,6,7])] #zip unpack values as tupes amd for caluse iterate throuh them?
print(f'new_list2={new_list2}')













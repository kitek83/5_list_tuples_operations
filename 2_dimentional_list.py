#2_dimentional_list.py
"""
Showing basic operations on 2 dimentional list. Lists can contain other lists as elements.
Two-dimentional lists (double-indexed lists,double-subscribed lists) require 2 indices
to identify an element.
"""
import numpy as np

a = [[77,68,86,73],
     [96,87,89,81],
     [70,90,86,81]]
print(f'a[1][0]={a[1][0]}')
#out: a[1][0]=96

#Following for statement outputs the rows of preceding two-dimensional list (m-by-n list) one row at a time
for row in a:
     for column in row:
          print(column, end=' ')
     print()
"""
out:
77 68 86 73 
96 87 89 81 
70 90 86 81 
"""
"""
task1
Let's modify the above nested loop to display the list's name  the row and column indices
and value of each element.
"""
for i,row in enumerate(a):
     for j,column in enumerate(row):
          print(f'a[{i}][{j}]={a[i][j]}',end=' ')
     print()
"""
out:
a[0][0]=77 a[0][1]=68 a[0][2]=86 a[0][3]=73 
a[1][0]=96 a[1][1]=87 a[1][2]=89 a[1][3]=81 
a[2][0]=70 a[2][1]=90 a[2][2]=86 a[2][3]=81 

"""
#for check
print(f'list(enumerate(a))={list(enumerate(a))}')
#out: list(enumerate(a))=[(0, [77, 68, 86, 73]), (1, [96, 87, 89, 81]), (2, [70, 90, 86, 81])]

"""
task2
Label the elements of the 2-by-3 list 'sales' to indicate the order in which 
they're set to 0 by the following program segment
"""
sales = [[2,3,4],
         [5,6,7]]

#for check:
print(f'len(sales)={len(sales)}')
#out: len(sales)=2

print(f'range(len(sales))={range(len(sales))}')
#out: range(len(sales))=range(0, 2)
print()

for row in range(len(sales)):
     for col in range(len(sales[row])):
          sales[row][col] = 0           #all indexes will == 0
          print(f'sales[{row}][{col}]={sales[row][col]}', end=' ')
     print()

print(f'range(len(sales[row]))={range(len(sales[row]))}')
#out:range(len(sales[row]))=range(0, 3)

print(f'sales={sales}')
"""
out:
sales[0][0]=0 sales[0][1]=0 sales[0][2]=0 
sales[1][0]=0 sales[1][1]=0 sales[1][2]=0 
"""
#out: sales=[[0, 0, 0], [0, 0, 0]]
print()

#2nd solution for task2 from above with the use of enumerate().

for i,row in enumerate(sales):
     for j,col in enumerate(row):
          sales[i][j] = 22              #enumerate() is much more safer,faster and easier to urdenstand solution
          print(f'sale[{i}][{j}]={sales[i][j]}', end=' ')
     print()
print(f'sales={sales}')

"""
out:
sale[0][0]=22 sale[0][1]=22 sale[0][2]=22 
sale[1][0]=22 sale[1][1]=22 sale[1][2]=22
"""
#out:sales=[[22, 22, 22], [22, 22, 22]]
print()

"""
Let's try to implement ndarray for the task2.
"""
#ndarray 2x3 with all indexes==0
nd_array = np.arange(6).reshape(2,3)
print(f'nd_array=\n{nd_array}')
"""
out:
nd_array=
[[0 1 2]
 [3 4 5]]
"""
for i,row in enumerate(nd_array):  #enumarate works fine with iterable ndarray
     for j,col in enumerate(row):
          print(f'nd_array[{i}][{j}]={nd_array[i][j]}', end=' ')
          nd_array[i][j] = 100
          print(f'changed_nd_array[{i}][{j}]={nd_array[i][j]}', end=' ')
     print()

"""
out:
nd_array[0][0]=0 changed_nd_array[0][0]=100 nd_array[0][1]=1 changed_nd_array[0][1]=100 nd_array[0][2]=2 changed_nd_array[0][2]=100 
nd_array[1][0]=3 changed_nd_array[1][0]=100 nd_array[1][1]=4 changed_nd_array[1][1]=100 nd_array[1][2]=5 changed_nd_array[1][2]=100 
"""
print()
"""
task3
Consider 2x3 integer list t.
Write a nested for statement that sets each element to the sum of
its' indices.
"""
t = [[1,2,3],
     [4,5,6]]
for i,row in enumerate(t):
     for j,col in enumerate(row):
          print(f'sum_t[{i}][{j}] =sum({i},{j})= {sum([i,j])}',end=' ')
     print()
"""
out:
sum_t[0][0] =sum(0,0)= 0 sum_t[0][1] =sum(0,1)= 1 sum_t[0][2] =sum(0,2)= 2 
sum_t[1][0] =sum(1,0)= 1 sum_t[1][1] =sum(1,1)= 2 sum_t[1][2] =sum(1,2)= 3 
"""
print()
#2nd solotion for task3
for row in range(len(t)):
     for col in range(len(t[row])):
          print(f't[{row}][{col}]={row}+{col}={row+col}', end=' ')
     print()

"""
out:
t[0][0]=0+0=0 t[0][1]=0+1=1 t[0][2]=0+2=2 
t[1][0]=1+0=1 t[1][1]=1+1=2 t[1][2]=1+2=3
"""
print()
#task4
"""
Given 2x3 integer t list.
a) Determine and display the average of t's elements using only nested for statement.
b)Write a for statement that determines and display the average of t's elements
  using the reductions sum and len to calculate the sum of each row's elements
  and the number of elements in eah row.
"""
#a)
t = [[10,7,3],
    [20,4,17]]

num = 0
total=0

for row in t:
     for col in row:
          total += col
          num += 1
average = total / num

print(f'average={total}/{num}={average:.2f}')
#out: average=61/6=10.17

#b)
print(len(t))  #shows 2 -> 2 rows

total=0
items = 0

for row in t:
     total += sum(row)
     items += len(row)

average = total/items
print(f'average2={total}/{items}={average:.2f}')
#out: average2=61/6=10.17

























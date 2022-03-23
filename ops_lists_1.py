#ops_lists_1.py
"""This program shows besic operations on lists.
This is a reminder."""

#list containing homegenous data
c = [-45,6,0,72,1543]

#list containing heterogenous data
d = ['Mary', 'Smith',3.57,2022]

print(f'list_c={c}')
print(f'list_d={d}')

#list length
print(f'len(c)={len(c)} len(d)={len(d)}')

#Accessing the list with negative indoces
print(f'c[-1]={c[-1]} c[-5]={c[-5]}')

print()
a = 1
b = 2
#use built in function sum
print(f'sum(c)={sum(c)}')
print(f'c[a+b]={c[a+b]}')  #will show 3rd index of list c

print()
#strings are immutable
s = 'hello'
# s[1] = 'd' --> TypeError
print(f's={s}')
print(f's[0]={s[0]}')

print()
#Appending to a list with +=
#use for statement and += to append values 1 through 5 to the list1
list1 = []
for num in range(1,6):
    list1 += [num]      #When the left operand of += is a list, the right operand must be iterable
print(f'list1={list1}')
print()

#string is iterable
p = 'python'
for i in p:
    print(i)

letters = []
letters += 'python'
print(f'letters={letters}')
print()

list2 = [10,20,30]
list3 = [40,22,3,50,60,5]
concatenated_list = list2 + list3
print(f'concatenated_list={concatenated_list}')
#using method sorted() to sort elements of collection
print(f'sorted(concatenated_list)={sorted(concatenated_list)}')

#list elements cen be accessed via their indices and the subscription operator ([])
s_concatenated_list = sorted(concatenated_list)   #sorted(iterable)
for i in range(len(s_concatenated_list)):
    print(f'index{i}={s_concatenated_list[i]}')
print()

#compare entire lists
list4 = [10,20,30]
print(f'list2==list4:{list2==list4}')
print(f'list2==list3:{list2==list3}')
print()























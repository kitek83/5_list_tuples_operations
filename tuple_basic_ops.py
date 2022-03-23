#tuple_basic_ops.py
"""This program shows basic operations on tuples."""
student_tuple = ()
print(f'len(student_tuple={len(student_tuple)}')

#pack a touple by seperating its values with commas
student_tuple = 'John', 'Greem',  3.3       #parentheses are optional
print(f'student_tuple={student_tuple}')

a_single_tuple = []
a_single_tuple = 'red',  #comma must follow the string, otherwise string is created
print(f'single_tuple={a_single_tuple}')
print()

#appending tuples to lists by augmented assignment statement
numbers1 = [10,20,30,40]
numbers1 += (5,6,7)
print(f'numbers1={numbers1}')
print(f'sorted(numbers1)={sorted(numbers1)}')
print()

#appending tuple to list using + operator
#result = [33,44,55] + (3,4,5)   #TypeError: can only concatenate list (not "tuple") to list
#print(f'result={result}')


#Tuples may contain mutable objects
students = ('Kate','John',[2,3,4])
#change 1st index of the list
students[2][1] = 85
print(f'student={students}')
print()

print(3*'------------unpack-------------')
#unpacking sequences - tuples
student_tuple = ('Amanda',[33,44,55])
name, grades = student_tuple   #unpacking
print(f'name:{name} grades:{grades}')
print()

#unpacks a string
first, second = 'hi'
print(f'{first}---{second}')

#unpack a list
names = ['Kris','Jack','Adam']
name1, name2, name3 = names
print(f'name1:{name1} name2:{name2} name3: {name3}')

#unpack sequence produced by range
print(f'range(10,40,10)={range(10,40,10)}')  #in this way function range is not working
num1,num2,num3 = range(10,40,10)            #in this way function range is working
print(f'num1={num1} num2={num2} num3={num3}')
print()

#Accessing indices and values woth built in function enumerate()
colors = ['red','orange','yellow']
#usinf built in function list to produce enumerate results
print(f'list(enumerate(colors))={list(enumerate(colors))}')

#similarly built int function tuple() creates tuple from sequence
print(f'tuple(enumerate(colors))={tuple(enumerate(colors))}')
print()

#for loop unpacks each touple returned by enumerate() into the variables index and value
for index,value in enumerate(colors):
    print(f'{index}:{value}')


























Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # program to create a list of n integer values
>>> number=[0,10,20,30,40,50,60,70,80,90]
>>> print(number)
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
\
>>> #Add an item in to the list of variables
>>> number.insert(10,100)
>>> number
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> number.append(110)
>>> number
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
>>> names=["Akki","siva","Deepak","balaji"]
>>> number.extends(names)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    number.extends(names)
AttributeError: 'list' object has no attribute 'extends'
>>> number.extend(names)
>>> number
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 'Akki', 'siva', 'Deepak', 'balaji']
>>> #Delete using a function
>>> del.number[5]
SyntaxError: invalid syntax
>>> del number[5]
>>> number
[0, 10, 20, 30, 40, 60, 70, 80, 90, 100, 110, 'Akki', 'siva', 'Deepak', 'balaji']
>>> number.remove(110)
>>> number
[0, 10, 20, 30, 40, 60, 70, 80, 90, 100, 'Akki', 'siva', 'Deepak', 'balaji']
>>> number.pop()
'balaji'
>>> #Store the largest number from the list to a variable
>>> list=[11,22,33,44,55,66,69]
>>> list
[11, 22, 33, 44, 55, 66, 69]
>>> a=max(list)
>>> print("the largest number from the list is:",a]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> print("the largest number from the list is:",a)
the largest number from the list is: 69
>>> b=min(list)
>>> print("The smallest number from the list is:",b)
The smallest number from the list is: 11
>>> #Create a tuple and print the reverse of the tuple
>>> tup=(1,2,3,4,5,6,7,8,9,10)
>>> tup
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> <class 'tuple'>
SyntaxError: invalid syntax
>>> type(tup)
<class 'tuple'>
>>> print('tuple in reverse:',t[::-1])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('tuple in reverse:',t[::-1])
NameError: name 't' is not defined
>>> print('tuple in reverse:',tup[::-1])
tuple in reverse: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> #Create a tuple and convert into list
>>> tuplee=(1,22,33,55,777,999)
>>> tuplee
(1, 22, 33, 55, 777, 999)
>>> list=[*tuplee]
>>> print("tuple into list:",list)
tuple into list: [1, 22, 33, 55, 777, 999]
>>> tuplee
(1, 22, 33, 55, 777, 999)
>>> list
[1, 22, 33, 55, 777, 999]
>>> 
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python script to merge two dictionaries
>>> Dict_1={1:"Akki",2:"Deepak"}
>>> Dict_2={3:"Siva",4:"Balaji"}
>>> Dict_1.update(Dict_2)
>>> Dict_1
{1: 'Akki', 2: 'Deepak', 3: 'Siva', 4: 'Balaji'}
>>> # program to remove a key from a dictionary
>>> Anime={1:"gojou",2:"itadori",3:"Sukuna",4:"Panda",5:"Mt.Fuji",6:"todou"}
>>> del Anime[5]
>>> Anime
{1: 'gojou', 2: 'itadori', 3: 'Sukuna', 4: 'Panda', 6: 'todou'}
>>> Anime.pop(6)
'todou'
>>> Anime
{1: 'gojou', 2: 'itadori', 3: 'Sukuna', 4: 'Panda'}
>>> Anime.clear()
>>> Anime
{}
>>> #Map two lists into a dictionary
>>> list_keys=["Akki","Deepak","Siva","Balaji"]
>>> list_values=[1,2,3,4]
>>> print("list of keys:",list_keys)
list of keys: ['Akki', 'Deepak', 'Siva', 'Balaji']
>>> print("list of values:",list_values)
list of values: [1, 2, 3, 4]
>>> res=dict(zip(list_keys,list_values))
>>> print("Dictionary from lists:",res)
Dictionary from lists: {'Akki': 1, 'Deepak': 2, 'Siva': 3, 'Balaji': 4}
>>> #Program to find the length of the set
>>> My_Set={"son goku","uzumaki naruto","mokey.D.Luffy","Gintama","Levi Ackerman","Gojou satoru","Eren jaegar"}
>>> len(My_set)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    len(My_set)
NameError: name 'My_set' is not defined
>>> len(My_Set)
7
>>> # Intersection of two sets
>>> Set_1={1,2,3,4,5,6}
>>> Set_2={2,4,6,8,10}
>>> Set_1 and Set_2
{2, 4, 6, 8, 10}
>>> Set_3=Set_1 & Set_2
>>> Print(Set_3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Print(Set_3)
NameError: name 'Print' is not defined
>>> print(Set_3)
{2, 4, 6}
>>> 
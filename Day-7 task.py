#Arithmetic operations using functions
def func(x,y):
    result=x+y
    print(x,"+",y,"=",result)
    result1=x-y
    print(x,"-",y,"=",result1)
    result2=x/y
    print(x,"/",y,"=",result2)
    result3=x*y
    print(x,"*",y,"=",result3)

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number"))
func(n1,n2)
# create function covid to accept patient name & temperature
     def covid(name, temp):
     print("patient name:", name)
     if temp == '':
          print("body temperature is : 98 degree")
     else:
           print("body temperature:", temp, "degree")

name = input("Enter the patients name:")
temp = input("Enter the body temperature:")
covid(name, temp)         

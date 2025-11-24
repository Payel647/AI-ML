#1
'''
name=input("Enter Your Name: ")
age=int(input("Enter Your Age: "))
print(f"Hello {name}, you are {age} years old!")
'''
#2
'''
a=int(input("Enter a Number: "))
b=int(input("Enter 2nd Number: "))
print(f"Sum={a+b}")
print(f"Difference={a-b}")
print(f"Product={a*b}")
print(f"Quotient={a/b}")
'''
#3
'''
a=float(input("Enter 1st Integer: "))
b=float(input("Enter 2nd Integer: "))
c=float(input("Enter Float Number: "))
print(f"Average: {(a+b+c)/3}")
'''
#4
'''
a=input("Enter a Number: ")
b=int(a)
c=float(a)
d=str(a)
print(f"{b} {type(b)}")
print(f"{c} {type(c)}")
print(f"{d} {type(d)}")
'''
#5
'''
x=10+3*2**2
print(x)
'''
#6
'''
a=int(input("Enter a Number: "))
b=int(input("Enter 2nd Number: "))
#Before Swapping 
print(f"Value of 1st Number : {a}\nValue of 2nd Number : {b}")
c=a
a=b
b=c
#After Swapping
print(f"Value of 1st Number : {a}\nValue of 2nd Number : {b}")
'''
#7
'''
a=float(input("Enter Temperature: "))
print(f"Fahrenheit: {((a*9)/5)+32}")
'''
#8
'''
a=float(input("Enter Radious : "))
print(f"Area of the Circle: {3.141*a**2}")
'''
#9
'''
p=float(input("Enter Principle: "))
r=float(input("Enter Interest Rate: "))
t=float(input("Enter time: "))
print(f"Simple Inerest: {(p*r*t)/100}")
'''
#10
'''
a=float(input("Enter Number: "))
print(f"Integer Part of {a} : {int(a)}\nFractional Part of {a} : {a-int(a)}")
'''

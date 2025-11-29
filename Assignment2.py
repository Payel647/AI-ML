#1
salary=int(input("Enter Salary: "))
if salary<30_000:
    print("tax: ",(salary*5*1)/100)
elif salary>=30_000 and salary<=70_000:
    print("tax: ",(salary*15*1)/100)
else:
    print("tax: ",(salary*25*1)/100)
#2
a=int(input("Enter starting range: "))
b=int(input("Enter ending range: "))
for i in range(a,b+1):
    if i%2==0:
        print(i)
#3
def print_digit(n):
    while(n>0):
        last=n%10
        n=n//10
        print(last)
n=int(input("Enter number: "))
print_digit(n)
#4
def count_digit(n):
    count=0
    while(n>0):
        last=n%10
        n=n//10
        count=count+1
    return count
n=int(input("Enter number: "))
print(count_digit(n))
#5
def sum_digit(n):
    sum=0
    while(n>0):
        last=n%10
        n=n//10
        sum=sum+last
    return sum
n=int(input("Enter number: "))
print(sum_digit(n))
#6
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
#7
while(True):
    n=input("Ente a Number or Quit: ")
    if n=="Quit":
        break
    else:
      n=int(n)
      if n<0:
         print("Negative")
      elif n>0:
         print("Positive")
      else:
         print("Zero")
#8
def calculator(a,b,o):
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        print("Invalid Operator!!")
a=int(input("Enter operand: "))
b=int(input("Enter 2nd Operand: "))
op=input("Enter Operator: ")
print("Result: ",calculator(a,b,op))
#9
a=int(input("Enter a Number: "))  
if a<=2 and a>0:
    print("Prime")
elif a<=0:
    print("Can't Say!!")
isTrue=True
for i in range(2,a):
    if a%i==0:
        print("Not a Prime")
        isTrue=False
        break
if(isTrue==True):
    print("Prime")
#10
res=46
while(True):
    n=int(input("Enter Number: "))
    if n>res:
        print("Too High!!")
    elif n<res:
        print("To Less!!")
    else:
        print("Correct!!")

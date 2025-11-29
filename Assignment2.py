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
        if(n==0):
            return 
        last=n%10
        n=n//10
        print_digit(n)
        print(last)
n=int(input("Enter number: "))
print_digit(n)
#4
def count_digit(n):
    if n==0:
        return 1;
    if n<0:
        n=-n
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
    if n<0:
        n=-n
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
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    elif o == '/':
        if b == 0:
            print("Division can not be done by 0")
            return -1
        else:
            return a/b
    else:
        print("Invalid Operator!!")
        return "Invalid"

a = int(input("Enter operand: "))
b = int(input("Enter 2nd Operand: "))
op = input("Enter Operator: ")

res = calculator(a, b, op) if calculator(a, b, op)!=-1 else "Invalid"

print("Result: ",res)
#9
a = int(input("Enter a Number: "))

if a <= 1:
    print("Not a Prime")
else:
    isPrime = True
    for i in range(2, a):
        if a % i == 0:
            print("Not a Prime")
            isPrime = False
            break
    if isPrime:
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
        break

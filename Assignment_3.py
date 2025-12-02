#1
s = input("Enter a string: ")

rev = s[::-1]

if s == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
#2
nums = input("Enter numbers separated by space: ")
nums = nums.split()

total = 0
count = 0

for x in nums:
    total += int(x)
    count += 1

print("Average =", total / count)
#3
list1 = input("Enter list 1: ").split()
list2 = input("Enter list 2: ").split()

merged = []

for x in list1:
    merged.append(int(x))

for x in list2:
    merged.append(int(x))

# sorting manually
for i in range(len(merged)):
    for j in range(i+1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

print("Merged & Sorted List:", merged)
#4
t = input("Enter tuple elements: ").split()

tup = ()
for x in t:
    tup += (int(x),)

even_tup = ()
odd_tup = ()

for x in tup:
    if x % 2 == 0:
        even_tup += (x,)
    else:
        odd_tup += (x,)

print("Even tuple:", even_tup)
print("Odd tuple:", odd_tup)
#5
students = {}

while True:
    print("\nA - Add Student")
    print("B - Update Marks")
    print("C - Search Student")
    print("D - Display All")
    print("E - Exit")

    ch = input("Enter choice: ").upper()

    if ch == 'A':
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Added.")

    elif ch == 'B':
        name = input("Enter name to update: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Updated.")
        else:
            print("Not found.")

    elif ch == 'C':
        name = input("Enter name to search: ")
        if name in students:
            print("Marks =", students[name])
        else:
            print("Not found.")

    elif ch == 'D':
        for name in students:
            print(name, ":", students[name])

    elif ch == 'E':
        break

    else:
        print("Invalid choice")
#6
words = ["apple", "banana", "kiwi", "cherry", "mango"]

d = {}
for w in words:
    d[w] = len(w)

print(d)
#7
s = input("Enter a string: ")

count = 0
for ch in s:
    if ch == " ":
        count += 1

print("Spaces:", count)
#8
l1 = input("Enter list 1: ").split()
l2 = input("Enter list 2: ").split()

s1 = set()
s2 = set()

for x in l1:
    s1.add(x)

for x in l2:
    s2.add(x)

if s1.isdisjoint(s2):
    print("No common elements")
else:
    print("They share common elements")
#9
nums = input("Enter numbers: ").split()

seen = set()
dup = set()

for x in nums:
    if x in seen:
        dup.add(x)
    else:
        seen.add(x)

print("Repeated elements:", list(dup))
#10
s = input("Enter a string: ")

unique_chars = []

for ch in s:
    if ch not in unique_chars:   # check manually
        unique_chars.append(ch)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))

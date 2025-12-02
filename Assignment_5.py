#1
# Write to file
with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter name: ")
        f.write(name + "\n")

# Read from file
with open("names.txt", "r") as f:
    data = f.read()
    print("Names in file:\n", data)
#2
# Append to log file
with open("log.txt", "a") as f:
    f.write("Program run successfully\n")

# Read the log file
with open("log.txt", "r") as f:
    print("Logs:")
    print(f.read())
#3
nums = [5, 10, 15, 20, 25]

new_list = [x for x in nums if x > 15]

print("Numbers greater than 15:", new_list)
#4
import json

cities = {
    "Kolkata": 4500000,
    "Delhi": 19000000,
    "Mumbai": 12500000
}

with open("cities.json", "w") as f:
    json.dump(cities, f)
with open("cities.json", "r") as f:
    data = json.load(f)

for city, pop in data.items():
    print(city, ":", pop)
new_city = input("Enter new city: ")
new_pop = int(input("Enter population: "))

data[new_city] = new_pop

with open("cities.json", "w") as f:
    json.dump(data, f)

print("Updated JSON saved.")
#5
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# Day 4 — Loops + Comprehensions

numbers = [1, 2, 3, 4, 5, 6]

squares = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
squares_even = [x ** 2 for x in numbers if x % 2 == 0]

users = [
    {"name": "Alex", "age": 17},
    {"name": "Kate", "age": 22},
    {"name": "John", "age": 19},
]

adults = [user["name"] for user in users if user["age"] >= 18]

labels = ["even" if x % 2 == 0 else "odd" for x in numbers]

names = ["Alex", "Kate", "John"]
ages = [17, 22, 19]

for index, name in enumerate(names, start=1):
    print(index, name)

pairs = [f"{name}: {age}" for name, age in zip(names, ages)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

flat = [item for row in matrix for item in row]
flat_even = [item for row in matrix for item in row if item % 2 == 0]

square_map = {item: item ** 2 for item in numbers if item % 2 == 0}

print(squares)
print(evens)
print(squares_even)
print(adults)
print(labels)
print(pairs)
print(flat)
print(flat_even)
print(square_map)

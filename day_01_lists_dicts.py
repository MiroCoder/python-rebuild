# Day 1 — Lists + Dicts

numbers = [5, 10, 15, 20]
numbers.append(25)
numbers[1] = 11
numbers.remove(15)
print(len(numbers))

user = {
    "name": "Mirik",
    "age": 23,
}

print(user.get("name"))
user["age"] = 24
user["city"] = "Mogilev"
user["active"] = True
del user["age"]

users = [
    {"name": "Alex", "age": 17},
    {"name": "Kate", "age": 22},
    {"name": "John", "age": 19},
]

adults = []
for item in users:
    if item["age"] >= 18:
        adults.append(item["name"])

print(adults)

words = ["cat", "dog", "cat", "bird", "cat"]
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

orders = [
    {"id": 1, "total": 120, "paid": True},
    {"id": 2, "total": 80, "paid": False},
    {"id": 3, "total": 250, "paid": True},
]

total_paid = 0
for order in orders:
    if order["paid"]:
        total_paid += order["total"]

print(total_paid)

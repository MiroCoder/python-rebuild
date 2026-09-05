# Day 5 — Dict Algorithms

words = ["api", "django", "api", "python", "django", "api"]
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

orders = [
    {"user": "Alex", "total": 100},
    {"user": "Kate", "total": 50},
    {"user": "Alex", "total": 70},
    {"user": "Kate", "total": 30},
    {"user": "John", "total": 200},
]

sales = {}
for order in orders:
    user = order["user"]
    if user in sales:
        sales[user] += order["total"]
    else:
        sales[user] = order["total"]

print(sales)

users = [
    {"name": "Alex", "city": "Minsk"},
    {"name": "Kate", "city": "Mogilev"},
    {"name": "John", "city": "Minsk"},
    {"name": "Anna", "city": "Mogilev"},
]

grouped = {}
for user in users:
    city = user["city"]
    if city in grouped:
        grouped[city].append(user["name"])
    else:
        grouped[city] = [user["name"]]

print(grouped)

lookup = {}
for index, user in enumerate(users, start=1):
    lookup[index] = user["name"]

print(lookup)

best_user = None
best_sales = -1
for user, total in sales.items():
    if total > best_sales:
        best_sales = total
        best_user = user

print(best_user, best_sales)

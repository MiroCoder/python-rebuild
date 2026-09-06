# Python Core mini-exam — progress
# Completed/corrected tasks from the current exam session.

# Task 1 — Lists + dicts
users = [
    {"name": "Alex", "age": 17},
    {"name": "Kate", "age": 23},
    {"name": "John", "age": 31},
    {"name": "Anna", "age": 19},
]

adult_names = [user["name"] for user in users if user["age"] >= 18]


# Task 2 — Strings
def normalize_username(text):
    return text.strip().lower().replace(" ", "_")


# Task 3 — Dict algorithm
def count_words(words):
    res = {}
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


# Task 4 — Exceptions
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


# Task 5–6 — OOP + inheritance
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0


class DiscountProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount

    def final_price(self):
        return self.price - (self.price * self.discount / 100)


# Task 8 — Sorting + lambda
products = [
    {"name": "Mouse", "price": 40},
    {"name": "Laptop", "price": 1200},
    {"name": "Keyboard", "price": 90},
]

sorted_products = sorted(
    products,
    key=lambda product: product["price"],
    reverse=True,
)


# Task 9 — any / all
users = [
    {"name": "Alex", "active": True},
    {"name": "Kate", "active": True},
    {"name": "John", "active": False},
]

has_inactive = any(not user["active"] for user in users)
all_active = all(user["active"] for user in users)


# Task 10 — Files
def read_lines(path):
    try:
        res = []
        with open(path, "r") as file:
            for line in file:
                res.append(line.strip())
        return res
    except FileNotFoundError:
        return []


# Task 11 — Comprehension
numbers = [3, 8, 11, 14, 20, 7]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]


# Task 12 — Dict aggregation
orders = [
    {"city": "Warsaw", "total": 100},
    {"city": "Berlin", "total": 200},
    {"city": "Warsaw", "total": 150},
    {"city": "Berlin", "total": 50},
    {"city": "Prague", "total": 80},
]

totals_by_city = {}
for order in orders:
    if order["city"] in totals_by_city:
        totals_by_city[order["city"]] += order["total"]
    else:
        totals_by_city[order["city"]] = order["total"]


# Task 14 — Data processing
users = [
    {"name": "Alex", "score": 70, "active": True},
    {"name": "Kate", "score": 95, "active": True},
    {"name": "John", "score": 100, "active": False},
    {"name": "Anna", "score": 85, "active": True},
]

best_active_user = max(
    (user for user in users if user["active"]),
    key=lambda user: user["score"],
)
best_active_name = best_active_user["name"]

# Task 7 is represented by the existing helpers package from Day 9.
# Task 13 still needs the no-positive-numbers edge case.
# Task 15 is still pending.

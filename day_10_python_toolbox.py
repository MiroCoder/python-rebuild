# Day 10 — Python Toolbox

# Sorting + key functions
users = [
    {"name": "Alex", "age": 31, "score": 72},
    {"name": "Kate", "age": 22, "score": 91},
    {"name": "John", "age": 27, "score": 84},
    {"name": "Anna", "age": 19, "score": 91},
]

by_age = sorted(users, key=lambda user: user["age"])
by_score = sorted(users, key=lambda user: user["score"], reverse=True)
youngest = min(users, key=lambda user: user["age"])

# any / all / max / sum
products = [
    {"name": "Laptop", "price": 1200, "stock": 4, "active": True},
    {"name": "Mouse", "price": 40, "stock": 0, "active": True},
    {"name": "Monitor", "price": 300, "stock": 7, "active": False},
    {"name": "Keyboard", "price": 90, "stock": 12, "active": True},
    {"name": "Headphones", "price": 150, "stock": 3, "active": True},
]

available_products = [
    product for product in products
    if product["active"] and product["stock"] > 0
]

names = [product["name"] for product in available_products]
sorted_by_price = sorted(
    available_products,
    key=lambda product: product["price"],
    reverse=True,
)
cheapest = min(available_products, key=lambda product: product["price"])
has_out_of_stock = any(product["stock"] == 0 for product in products)
all_have_stock = all(product["stock"] > 0 for product in products)
total_stock = sum(product["stock"] for product in products)

# Integrated backend-style task
users = [
    {"id": 1, "name": "Alex", "active": True},
    {"id": 2, "name": "Kate", "active": True},
    {"id": 3, "name": "John", "active": False},
    {"id": 4, "name": "Anna", "active": True},
]

orders = [
    {"id": 101, "user_id": 1, "total": 120, "paid": True},
    {"id": 102, "user_id": 2, "total": 80, "paid": False},
    {"id": 103, "user_id": 1, "total": 200, "paid": True},
    {"id": 104, "user_id": 3, "total": 300, "paid": True},
    {"id": 105, "user_id": 4, "total": 50, "paid": True},
    {"id": 106, "user_id": 2, "total": 150, "paid": True},
]

active_users = [user for user in users if user["active"]]
paid_orders = [order for order in orders if order["paid"]]
active_user_ids = [user["id"] for user in active_users]
active_paid_orders = [
    order for order in paid_orders
    if order["user_id"] in active_user_ids
]

total_revenue = sum(order["total"] for order in active_paid_orders)
largest_active_order = max(
    active_paid_orders,
    key=lambda order: order["total"],
)
sorted_active_orders = sorted(
    active_paid_orders,
    key=lambda order: order["total"],
    reverse=True,
)

inactive_users = [user for user in users if not user["active"]]
inactive_user_ids = [user["id"] for user in inactive_users]
inactive_paid_orders = [
    order for order in paid_orders
    if order["user_id"] in inactive_user_ids
]
has_inactive_paid_order = any(order["paid"] for order in inactive_paid_orders)

all_active_users_have_orders = all(
    any(order["user_id"] == user["id"] for order in orders)
    for user in active_users
)

revenue_by_user = {}
for order in active_paid_orders:
    if order["user_id"] in revenue_by_user:
        revenue_by_user[order["user_id"]] += order["total"]
    else:
        revenue_by_user[order["user_id"]] = order["total"]

best_user_id = max(
    revenue_by_user,
    key=lambda user_id: revenue_by_user[user_id],
)

best_user_name = next(
    user["name"]
    for user in users
    if user["id"] == best_user_id
)

result = {
    "total_revenue": total_revenue,
    "largest_order": largest_active_order,
    "best_user": best_user_name,
    "has_inactive_paid_order": has_inactive_paid_order,
}

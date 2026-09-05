# Day 3 — Functions


def greet(name):
    return f"Hello, {name}"


def multiply(a, b):
    return a * b


def is_adult(age):
    return age >= 18


def power(number, exponent=2):
    return number ** exponent


def get_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


def get_adults(users):
    result = []
    for user in users:
        if user["age"] >= 18:
            result.append(user["name"])
    return result


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "F"


def total(*args):
    return sum(args)


def show_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")


def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


if __name__ == "__main__":
    print(greet("Miro"))
    print(multiply(4, 5))
    print(power(2, 3))
    print(get_even([1, 2, 3, 4, 5, 6]))
    print(find_max([4, 10, 2, 17, 8]))

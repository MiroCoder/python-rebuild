# Day 6 — Exceptions + Files


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "error"


def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "not found"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(to_int("25"))
print(to_int("hello"))

# File modes:
# r = read
# w = write/overwrite
# a = append

with open("stack.txt", "a", encoding="utf-8") as file:
    file.write("django\n")

lines = []
try:
    with open("stack.txt", "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())
except FileNotFoundError:
    pass

print(lines)

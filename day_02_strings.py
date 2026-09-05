# Day 2 — Strings

text = "  Hello Python  "
print(text.strip().lower())

stack = "python django fastapi"
words = stack.split()
print(words)
print("-".join(words))

message = "I like Java"
print(message.replace("Java", "Python"))

text = "hello world"
vowels = ["a", "e", "i", "o", "u"]
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)

text = "python"
result = ""
for char in text:
    result = char + result

print(result)


def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("level"))
print(is_palindrome("python"))

text = "banana"
counts = {}
for char in text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)

text = "  Python is FUN  "
new_text = text.strip().lower().split()
result = "-".join(new_text)
print(result)

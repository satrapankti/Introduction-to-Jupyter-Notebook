# Approach 1
r = range(1, 11)
result = []

for item in r:
    result.append(item * item)

print(result)


# Approach 2 (Using List Comprehension)
result = [item * item for item in range(1, 11)]
print(result)

print([item * item for item in range(1, 11)])

# ----------------------------------------------------------
# Get list of even numbers from the range 1, 11
result = []
for item in range(1, 11):
    if item % 2 == 0:
        result.append(item)

print(result)

# Approach 2
result = [item for item in range(1, 11) if item % 2 == 0]
print(result)

# ----------------------------------------------------------
# Using LC, generate a list of ["www.amazon.in", "www.flipkart.in", "www.paytm.in"]

websites = ["amazon", "flipkart", "paytm"]

result = ["www." + web + ".in" for web in websites]
print(result)

# ----------------------------------------------------------
# [("Welcome", 7), ("to", 2), ("the", 3), ("world", 5), ("of", 2), ...]

s = "Welcome to the world of Python Programming"

# Approach 1:
lstWords = s.split(" ")
print(lstWords)
result = []
for item in lstWords:
    result.append((item, len(item)))

print(result)

# Approach 2
result = [(item, len(item)) for item in lstWords]
print(result)


result = [(item, len(item)) for item in s.split(" ")]
print(result)

# ----------------------------------------------------------
# Given the subject = "MATHEMATICS", print all the consonants in a list
# Vowels : A E I O U
# ["M", "T", "H", "M", "T", "C", "S"]

subject = "MATHEMATICS"
result = []

for item in subject:
    if item == "A" or item == "E" or item == "I" or item == "O" or item == "U":
        continue

    result.append(item)

print(result)

result = []
for item in subject:
    if item in "AEIOUaeiou":
        continue

    result.append(item)
print(result)

result = []
for item in subject:
    if item not in "AEIOUaeiou":
        result.append(item)

print(result)

# ----------------------------------------------------------
# Dictionary Comprehension

# Take an integer input from the user, lets say user has entered number 10
# Generate an output like below:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, .... , 10: 100}

n = int(input("Enter any number: "))
result = {}

for item in range(1, n + 1):
    result[item] = item * item

print(result)

# Approach 2 Using DC
result = { item: item * item for item in range(1, n + 1)}
print(result)

# ----------------------------------------------------------

s = "the quick brown fox jumps over the lazy dog"

result = {item: s.count(item) for item in s}
print(result)
print(len(result))

# ----------------------------------------------------------

alphabets = ["a", "b", "c", "d"]
fruits = ["apple", "banana", "cherry", "dates"]

# using the above two lists, create a dictionary

result = {alphabets[item]: fruits[item] for item in range(4)}
print(result)

# ----------------------------------------------------------

alphabets = ["a", "b", "c", "d", "p"]
fruits = ["apple", "banana", "cherry", "dates", "papaya"]

# {"a": ("apple", 5), "b": ("banana", 6), ...}

result = {alphabets[item]: (fruits[item], len(fruits[item])) for item in range(4)}

print(result)

result = {alphabets[item]: (fruits[item], len(fruits[item])) for item in range(len(fruits))}

print(result)

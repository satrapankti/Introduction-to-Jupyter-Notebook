f = lambda num: num + num
print(f(10))

addNos = lambda x, y: x + y
print(addNos(3, 5))

mx = lambda x, y: x if x > y else y
print(mx(18, 21))

# ----------------------------------------------------------

nums = list(range(1, 11))
print("Numbers: ", nums)

sq = lambda a: a * a

# mobj = map(sq, nums)
mobj = map(sq, range(1, 11))
print("Map Object   : ", mobj)
print("Type of mobj : ", type(mobj))

# print("List of Square of numbers using Map: ", list(mobj))
print("List of Tuple  of numbers using Map: ", tuple(mobj))

# ----------------------------------------------------------

nums = list(range(1, 11))

print("Numbers : ", nums)

even = lambda num: num % 2 == 0

print(even(5))
print(even(10))

result = filter(even, nums)

print("Result using filter - even : ", result)
# print("List from result           : ", list(result))
print("Tuple from result          : ", tuple(result))

#=======================

result = map(even, nums)
print("Result using map - even    : ", result)
print("List from result map       : ", list(result))

# ----------------------------------------------------------

from functools import reduce

nums = list(range(1, 11))
print("Numbers : ", nums)

addNos = lambda x, y: x + y
print(addNos(100, 200))

result = reduce(addNos, nums)
print("Result : ", result)

# ----------------------------------------------------------
# num = input("Enter the string that needs search  : ")
num = "Count"
search = open("Functions.py", "r")
result = ""
for line in search:
    if num in line:
        print(line)
        result += line
search.close()

r = open("result.txt", "a")
r.write(result)
r.close()

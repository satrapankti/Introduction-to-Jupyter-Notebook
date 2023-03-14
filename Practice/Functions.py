# Functions == methods

def myFunction():
    print("Inside myFunction")


myFunction()

# ----------------------------------------------------------
# Write a function to find maximum of two numbers

def findMaximum(x, y):
    if x > y:
        return x
    else:
        return y


result = findMaximum(3, 5)
print("Result: ", result)

# ----------------------------------------------------------
# Factorial of number
# 5! = 5 * 4 * 3 * 2 * 1
# 1! = 1
# 0! = 1

def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result


n = int(input("Enter any number: "))
r1 = iterFactorial(n)
# print(result)
output = "Factorial of " + str(n) + " is " + str(r1)
print(output)
print("Factorial of {} is {}".format(n, r1))

# ----------------------------------------------------------
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 1! = 0! = 1
# n1 = n * (n-1)!

def recurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recurFactorial(num - 1)


n = int(input("Enter any number: "))
print("Factorial of {} is {}".format(n, recurFactorial(n)))

# rf(5)
# 5
# 5 * rf(4)
# 4 * rf(3)
# 3 * rf(2)
# 2 * rf(1)
# 1 * rf(0)

# ----------------------------------------------------------

def defaultArgFunction(x=1000):
    print("The value of x is : ", x)


defaultArgFunction(10)
defaultArgFunction()

# ----------------------------------------------------------

def namedArgumentFunction(a, b, c):
    print("The values are a: {}, b: {}, c: {}".format(a, b, c))


namedArgumentFunction(100, 200, 300)  # Positional Arguments
namedArgumentFunction(c=1000, a=800, b=900)  # Named Arguments
# Mix of Positional And Named Arguments
# Rule: Always specify positional arguments first, and then specify the named arguments
# namedArgumentFunction(101, a=102, c=103) # error

# namedArgumentFunction(a=500, 600, c=700)  #error
namedArgumentFunction(123, c=789, b=456)

# ----------------------------------------------------------

# Lambda Functions
# Anonymous functions
# Functions which have got NO names
# They are used to write one-line functions

def GetSquare(num):
    return num * num


print(GetSquare(7))

f = lambda num: num * num
print(f)
print(type(f))
result = f(9)
print("Square of number: ", result)

print("Square of number: ", (lambda num: num * num)(10))
print("Square of number: ", (lambda num: num * num)(int(input("Enter any number: "))))

f = lambda x, y: x if x > y else y
print("Max of 3, 5 is: ", f(3, 5))

# ----------------------------------------------------------
# Function as a PARAMETER

def GetSquare(num):
    return num * num


def GetCube(num):
    return num * num * num

GetSquare(5)


def WrapperFunction(funcAsParam, num):
    # funcAsParam = GetSquare
    # num = 5
    # GetSquare(5)
    return funcAsParam(num)


result = WrapperFunction(GetSquare, 5)
print("Result: ", result)

result = WrapperFunction(GetCube, 5)
print("Result: ", result)


# Functions are also called as First Class Objects in Python
# Function as arguments
# Function can be returned
# Closures
# Decorators

lstFunc = [GetSquare, GetCube]
print(lstFunc)
for item in lstFunc:
    print("Result of iteration: ", item(10))

# ----------------------------------------------------------
# Args
# Packing

def SumOfNumbers(*args):
    print("Args: ", args)
    print("Type of Args: ", type(args))
    result = 0
    for item in args:
        result += item

    print("Sum of passed numbers: ", result)


SumOfNumbers(1, 2, 3)
SumOfNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# ----------------------------------------------------------
# Args

def printPlayerDetails(name, age, team):
    print("Player Details, Name: {}, Age: {}, Team: {}".format(name, age, team))


printPlayerDetails("Virat", 31, "RCB")

msd = ("MS Dhoni", 37, "CSK")
printPlayerDetails(msd[0], msd[1], msd[2])

printPlayerDetails(*msd) # Unpacking

# ----------------------------------------------------------
# kwargs == dictionary

def printStudentDetails(**kwargs): # Receiver - Pack
    print("kwargs: ", kwargs)
    print("Type of kwargs: ", type(kwargs))
    print("Student Details: Name: {}, Age: {}, Marks: {}, Stream: {}".format(
        kwargs["name"], kwargs['age'], kwargs['marks'], kwargs['stream']
    ))


printStudentDetails(name="Mary", age=15, marks=500, stream="CSE")

d = {'name': 'John', 'age': 17, 'marks': 700, 'stream': 'ECE'}
printStudentDetails(**d) # Caller - Unpack

# ----------------------------------------------------------

def printStudentDetails(name, age, marks, stream):
    print("Student Details. Name: {}, Age: {}, Marks: {}, Stream: {}".format(
        name, age, marks, stream ))


printStudentDetails("Mary", 10, 500, "CSE")

d = {'name': 'John', 'age': 17, 'marks': 700, 'stream': 'ECE'}
printStudentDetails(d["name"], d['age'], d['marks'], d['stream'])
printStudentDetails(**d)  # Caller - Unpack

# ----------------------------------------------------------

def EmptyListAsParam(my_list=[]):
    my_list.append("$")
    return my_list


r = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r)

r1 = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r1)

r2 = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r2)

r3 = EmptyListAsParam([1, 2, 3])
print("Returned Output 1st Iteration: ", r3)

r4 = EmptyListAsParam([1, 2, 3])
print("Returned Output 1st Iteration: ", r4)

# ----------------------------------------------------------

def EmptyListAsParam(my_list=None):
    if my_list is None:
        my_list = []

    my_list.append("$")
    return my_list


r = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r)

r1 = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r1)

r2 = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r2)

r3 = EmptyListAsParam([1, 2, 3])
print("Returned Output 1st Iteration: ", r3)

r4 = EmptyListAsParam([1, 2, 3])
print("Returned Output 1st Iteration: ", r4)

# ----------------------------------------------------------

def multipleUnpackings(*args):  # Receiver - Pack
    print("Args: ", args)
    print("Type of Args: ", type(args))


a = [1, 2, 3]
multipleUnpackings(*a)  # Caller - Unpack


b = (4, 5, 6)
multipleUnpackings(*b)  # Caller - Unpack


c = {4, 5, 6}
multipleUnpackings(*c)  # Caller - Unpack

# Python 3.5 ==> This feature is available ONLY from Python 3.5

print(*range(1, 6), sep="\n")

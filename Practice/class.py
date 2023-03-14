'''
Mould => Idol
Class => Object

10
iter 1:
input = Name
grades = 1, 2, 3

iter 2:
input = Name
grades = 1, 2, 3

[
{"name": value, "grades": [1, 2, 3],
{"name": value, "grades": [1, 2, 3],
{"name": value, "grades": [1, 2, 3],
{"name": value, "grades": [1, 2, 3],
{"name": value, "grades": [1, 2, 3],

]

[
s1
s2
s3
]

'''

# -----------------------------------------------------------------------------------

class Employee:
    pass

e1 = Employee()
e2 = Employee()

print("Employee e1: ", e1)
print("Employee e2: ", e2)

print("Type of e1 : ", type(e1))
print("Type of e2 : ", type(e2))

# -----------------------------------------------------------------------------------

class Employee:
    '''
    Help: An Employee class documentation
    The instance of class can be used to create and manage Employee data
    It stores info like, name, address, education details etc
    '''
    pass


e1 = Employee()
print("Employee e1   : ", e1)
print("Type of e1    : ", type(e1))
print("Employee doc  : ", Employee.__doc__)
print("---------------------------------------")
print("e1 doc        : ", e1.__doc__)

# -----------------------------------------------------------------------------------

class Employee:
    '''
    Help: An Employee class documentation
    The instance of class can be used to create and manage Employee data
    It stores info like, name, address, education details etc
    '''
    def __init__(self, firstName, lastName):
        # Similar to constructor
        # print("Value of self: ", self)
        self.fn = firstName
        self.ln = lastName


e1 = Employee("Virat", "Kohli")
e2 = Employee("MS", "Dhoni")

print("e1 : ", e1)
print("e2 : ", e2)

print("e1 dict              : ", e1.__dict__)
print("e2 dict              : ", e2.__dict__)
print("Employee dict        : ", Employee.__dict__)

# -----------------------------------------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def addGrade(self, grade):
        self.grades.append(grade)

    def getAverage(self):
        if len(self.grades):
            return sum(self.grades) / len(self.grades)
        else:
            return "empty grades"



s1 = Student("Virat")
s2 = Student("MS Dhoni")

print("s1 dict      : ", s1.__dict__)
s1.addGrade(10)
s1.addGrade(20)
s1.addGrade(30)
print("s1 dict after adding grades     : ", s1.__dict__)
print("s2 dict after adding grades     : ", s2.__dict__)

print("S1 Average: ", s1.getAverage())
print("S2 Average: ", s2.getAverage())

import math
math.factorial(10)

# -----------------------------------------------------------------------------------

class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salary
        self.email = self.fn + "." + self.ln + "@gmail.com"

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("e1 dict : ", e1.__dict__)

# -----------------------------------------------------------------------------------

class Employee:
    employee_count = 0

    def __init__(self, firstName, lastName, age, salray):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salray
        self.email = self.fn + "." + self.ln + "@gmail.com"
        Employee.employee_count += 1

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("Employee dict: ", Employee.__dict__)
print("e1 dict : ", e1.__dict__)

e2 = Employee("MS", "Dhoni", 35, 7000)
print("Employee dict after MSD: ", Employee.__dict__)

print("Employee count using e1 (instance/object) : ", e1.employee_count)

# -------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, firstName, lastName, age, salray):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salray
        self.email = self.fn + "." + self.ln + "@gmail.com"

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


# Inherited / Derived / Subclass / Child / Extend
class Developer(Employee):
    pass

e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()

e2 = Developer("Ashwin", "R", 33, 6000)
e2.printDetails()

# ------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, firstName, lastName, age, salray):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salray
        self.email = self.fn + "." + self.ln + "@gmail.com"

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


# Inherited / Derived / Subclass / Child / Extend
class Developer(Employee):
    def __init__(self, firstName, lastName, age, salary, proglang):
        super().__init__(firstName, lastName, age, salary)
        # Employee.__init__()
        self.proglang = proglang

    def printDetails(self):
        super().printDetails()
        print("Programming Language: ", self.proglang)


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()

e2 = Developer("Ashwin", "R", 33, 6000, "Python")
e2.printDetails()

# To find the Parent
print("Parent of Developer: ", Developer.__base__)

# To find instance details
print("Is e2 instance of Developer : ", isinstance(e2, Developer))
print("Is e2 instance of Employee  : ", isinstance(e2, Employee))

print("Is Developer subclass of Employee : ", issubclass(Developer, Employee))
print("Is Employee subclass of Developer : ", issubclass(Employee, Developer))

# -------------------------------------------------------------------------------------------------
# abc is abstract base class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def printName(self):
        print("I am in shape class")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Square Area  : ", self.length * self.length)


class Rectange(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectange Area  : ", self.length * self.breadth)


# s1 = Shape()
sq1 = Square(5)
sq1.area()
r1 = Rectange(3, 5)
r1.area()

# -------------------------------------------------------------------------------------------------
# Monkey Patching

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Virat")
s2 = Student("Dhoni")

s2.age = 37

print("s1 dict          : ", s1.__dict__)
print("s2 dict          : ", s2.__dict__)

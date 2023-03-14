usrList = [9, 1, 8, 2, 7, 3, 6, 4, 5]

print("Original List : ", usrList)

s_li = sorted(usrList)  # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Original List : ", usrList)

print("Sorting using inbuild sort method")

usrList.sort() # IN-PLACE SORTING
print("Original List : ", usrList)

# --------------------------------------------------------------------------

usrTuple = (9, 1, 8, 2, 7, 3, 6, 4, 5)

print("Original Tuple : ", usrTuple)

s_li = sorted(usrTuple, reverse=True)  # NON-INPLACE SORTING

print("Sorted List    : ", s_li)
print("Original Tuple : ", usrTuple)
print("Sorted Tuple   : ", tuple(s_li))

# There is no IN-PLACE sorting for tuple (as tuples are IMMUTABLE)

# ------------------------------------------------------------------------------

usrList = [9, 1, 8, 2, 7, 3, 6, 4, 5]

print("Original List : ", usrList)

s_li = sorted(usrList, reverse=True)  # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Original List : ", usrList)

print("Sorting using inbuild sort method")

usrList.sort(reverse=True) # IN-PLACE SORTING
print("Original List : ", usrList)

# --------------------------------------------------------------------------
# Sorting on dictionaries
d = {"A": 1, "D": 4, "B": 2, "C": 3}

print("Original Dict                 : ", d)
s_d = sorted(d)
s_d_values = sorted(d.values())

print("Sorted function on d (keys)   : ", s_d)
print("Sorted function on d (values) : ", s_d_values)

# ----------------------------------------------------------

usrList = [-9, 1, 8, 2, -7, 3, 6, -4, 5, 4]

print("Original List : ", usrList)

s_li = sorted(usrList, key=abs)  # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Original List : ", usrList)

print("Sorting using inbuilt sort method")

usrList.sort(key=abs) # IN-PLACE SORTING
print("Original List : ", usrList)

# ---------------------------------------------------------------------------

usrSet = {9, 1, 8, -2, 7, 3, -6, 4, 5}

print("Original Set  : ", usrSet)

s_li = sorted(usrSet)  # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Original Set  : ", usrSet)

# -----------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # dunder methods
    def __repr__(self):
        return "{}-{}-{}".format(self.name, self.age, self.salary)


e1 = Employee("ABC", 25, 700)
e2 = Employee("XYZ", 55, 7000)
e3 = Employee("DEF", 65, 70)

lstEmp = [e1, e2, e3]

print("List of Employees        : ", lstEmp)

def sortKeyEmployeeName(emp):
    return emp.name

def sortKeyEmployeeAge(emp):
    return emp.age

def sortKeyEmployeeSalary(emp):
    return emp.salary

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName)
print("Sorted list of Employees (name)              : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge)
print("Sorted list of Employees (age)               : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary)
print("Sorted list of Employees (salary)            : ", sortedLstEmp)

print("Reverse Sorting")
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName, reverse=True)
print("Sorted list of Employees (name)              : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge, reverse=True)
print("Sorted list of Employees (age)               : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary, reverse=True)
print("Sorted list of Employees (salary)            : ", sortedLstEmp)

print("IN PLACE SORTING")
lstEmp.sort(key=sortKeyEmployeeName)
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=sortKeyEmployeeAge)
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=sortKeyEmployeeSalary)
print("Sorted List of Employees (Salary)      : ", lstEmp)

print("----------------------------------------")
print("IN PLACE LAMBDA SORTING")
lstEmp.sort(key=lambda emp: emp.name)
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=lambda emp: emp.age)
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=lambda emp: emp.salary)
print("Sorted List of Employees (Salary)      : ", lstEmp)

# ---------------------------------------------------------------------------------------------

from operator import attrgetter

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "{}-{}-{}".format(self.name, self.age, self.salary)


e1 = Employee("ABC", 25, 700)
e2 = Employee("XYZ", 55, 7000)
e3 = Employee("DEF", 65, 70)

lstEmp = [e1, e2, e3]

print("List of Employees        : ", lstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("name"))
print("Sorted list of Employees (Name)          : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("age"))
print("Sorted list of Employees (Age)           : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("salary"))
print("Sorted list of Employees (Salary)        : ", sortedLstEmp)

print("IN PLACE SORTING")
lstEmp.sort(key=attrgetter("name"))
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=attrgetter("age"))
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=attrgetter("salary"))
print("Sorted List of Employees (Salary)      : ", lstEmp)

# --------------------------------------------------------------------------------------------------

from operator import itemgetter

lstEmp = [("ABC", 25, 700), ("DEF", 65, 70), ("XYZ", 55, 7000)]

print("Original List of Employees       : ", lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(0))
print("Sorted List of Employees (name)      : ", s_lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(1))
print("Sorted List of Employees (age )      : ", s_lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(2))
print("Sorted List of Employees (salary)    : ", s_lstEmp)

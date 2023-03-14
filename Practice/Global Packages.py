def myFunction():
    a = "Welcome"
    print("The value of a: ", a)
    print("Inside myFunction")


myFunction()

# print(a) ## Error, the scope of a is with in myFunction

# ----------------------------------------------------------

def myFunction():
    global temp
    temp = "100"
    print("The value of temp inside myFunction is : ", temp)


myFunction()

print("The value of temp outside myFunction is : ", temp)

# ----------------------------------------------------------

runscored = 1


def localFunction():
    runscored = 2
    print("The value of runscored in localFunction is : ", runscored)


def globalFunction():
    global runscored
    runscored = 3
    print("The value of runscored in globalFunction is : ", runscored)


print("The value of runscored in main : ", runscored)

localFunction()

print("After calling localFunction, The value of runscored in main : ", runscored)

globalFunction()

print("After calling globalFunction, The value of runscored in main : ", runscored)

localFunction()

print("After calling localFunction, The value of runscored in main : ", runscored)

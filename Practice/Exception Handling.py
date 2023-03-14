usrInput = input("Enter any number: ")
result = 100 / int(usrInput)
print("Result : ", result)

# ----------------------------------------------------------

try:
    usrInput = input("Enter any number: ")
    result = 100 / int(usrInput)
    print("Result : ", result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Please enter numbers greater than zero.")

# ----------------------------------------------------------

try:
    fh = open("ExceptionHandling.txt", "w")
    fh.write("Opening the file.\n")

    usrInput = input("Enter any number: ")
    fh.write("The user entered number is : " + usrInput + "\n")

    result = 100 / int(usrInput)

    # fh.write("The result is : " + str(result) + "\n")
    output = "The result is : {} \n".format(result)
    fh.write(output)
    print("Result : ", result)

except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Please enter numbers greater than zero.")
finally:
    fh.write("Closing the file.\n")
    fh.close()

number = int(input("Enter any number: "))

if number > 10:
    print("Number is greater than 10")
else:
    print("Number is less than 10.")

# ----------------------------------------------------------

number = int(input("Enter any number: "))

if number > 0:
    print("Positive Number.")
elif number == 0:
    print("Zero")
else:
    print("Negative Number.")

# ----------------------------------------------------------
# While

index = 1
while index < 10:
    print(index)
    index += 1  # index = index + 1

# ----------------------------------------------------------
# range

r = range(5, 50, 10)
for item in r:
    print(item)

# ----------------------------------------------------------

websites = ["amazon", "flipkart", "paytm"]

# www.amazon.com
# www.flipkart.com
# www.paytm.com
for item in websites:
    print("www." + item + ".com")

# ----------------------------------------------------------

websites = ["amazon", "flipkart", "paytm"]
extensions = ["org", "com", "in"]

for web in websites:
    for ext in extensions:
        print("www." + web + "." + ext)


# ----------------------------------------------------------

languages = ["C", "C++", "Python", "Java", "Golang"]

for index, element in enumerate(languages):
    print(index, element)

# ----------------------------------------------------------

r = range(10)

for item in r:
    print(item)
    if item == 5:
        break

# ----------------------------------------------------------

for item in range(10):
    if item % 2 == 0:
        continue
    print(item)

# ----------------------------------------------------------

details = {"Name": "Rohit", "Age": 34, "Team": "MI", "50s": 4}

print("Iterating through keys")
for item in details:
    print(item)

print("------------------------------")
for item in details.values():
    print(item)

print("------------------------------")
for key, value in details.items():
    print(key, value)

# ----------------------------------------------------------
# Write a program to print the below pattern
# *
# * *
# * * *
# * * * *
# * * * * *

# For loop
# * operator
for item in range(1, 6):
    print("* " * item)

# ----------------------------------------------------------
# Write a program to print the below pattern

  #           *
  #         *   *
  #       *   *   *
  #    *    *    *   *
  # *     *    *   *   *

for item in range(1, 6):
    s1 = " " * (5 - item) # Space
    s2 = "* " * item  # *

    print(s1 + s2)

# S = ["     ", "   ", "  ", " ", ""]
# for item in range(1, 5):
#     print(S[item] + "* " * item)

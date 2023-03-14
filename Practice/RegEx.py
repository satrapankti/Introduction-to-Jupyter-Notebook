'''
Identifiers: (To look out for something)
\d      Any Number
\D      Anything but a Number
\s      Space
\S      Anything but a Space
\w      Any Character
\W      Anything but a Character
.       any character, except for a newline
\b      The whitespace around Words
\.      a period

Modifiers: (To look for the count)
{1,3}   Expecting 1-3 ex. \d{1,3}
+       Match 1 or more
?       Match 0 or 1
*       Match 0 or more
$       Match the end of a string
^       Match the beginning of a string
|       Either or
[]      range or "variance" [A-Z], [A-Za-z], [1-5], [1-5a-eA-Z]
{n}     expecting "n" amount ex. \d{4}

White Space Characters:
\n      new line
\s      space
\t      tab
\e      escape
\f      form feed
\r      carriage return

DONT FORGET THE BELOW CHARACTERS (Use Escape characters to use them) (. + * ? [ ] $ ^ ( ) { } | \ )
''' 

s = "Welcome   to Regex   Programming   using Python"
lstWords = s.split(" ")
print(lstWords)

# -----------------------------------------------------------------------------------

import re

s = "Welcome   to  Regex   Programming   using Python"

print("The value of s    : ", s)
lstValues = re.split(r"\s", s)
print("Regex split using '\s'   : ", lstValues)

lstValues = re.split(r"\s+", s)
print("Regex split using '\s+'   : ", lstValues)

lstValues = re.split(r"(\s+)", s)
print("Regex split using '(\s+)'   : ", lstValues)

# GREP => Global Regular Expression Print
lstValues = re.split(r"s+", s)
print("Regex split using 's+'   : ", lstValues)

s = "Welcome to Regex Programming using Python"
lstValues = re.split(r"[a-f]", s)
print("Regex split using '[a-f]'   : ", lstValues)

lstValues = re.split(r"([a-f])", s)
print("Regex split using '([a-f])'   : ", lstValues)

lstValues = re.split(r"[a-f][l-n]", s)
print("Regex split using '[a-f][l-n]'   : ", lstValues)

# -----------------------------------------------------------------------------------

import re

address = "Hi 11  89 Main, 4th Cross, 123 Road, Marathalli, 5678 Bangalore, 560023 67893"

lstValues = re.findall(r"\d+", address)
print("findall using \d+ : ", lstValues)

lstValues = re.findall(r"\d{6}", address)
print("findall using \d{6} : ", lstValues)


lstValues = re.findall(r"\d{2}", address)
print("findall using \d{2} : ", lstValues)

lstValues = re.findall(r"\d{1,6}", address)
print("findall using \d{1,6} : ", lstValues)

# -----------------------------------------------------------------------------------

import re

s = '''
<html>
<head>
<title>Current IP Address Allocations
</title>
</head>
<body>
IP Address are 172.45.78.109
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 11.67.98.102
Computer 2: 10.68.98.102
</body>
</html>
'''

# IP Address : 4 Parts : 2-3 digits
lstValues = re.findall(r"\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}", s)
print("IP Address: ", lstValues)

lstValues = re.findall(r"10.\d{2,3}\.\d{2,3}\.\d{2,3}", s)
print("IP Address: ", lstValues)

# -----------------------------------------------------------------------------------

import re

empDetails = "Hi I have a credit card with number 3775 123456 78910 and " \
             "other card is" \
             " 3545 456789 12345"

#http://www.getcreditcardnumbers.com

# AMEX Card
# Always Start with 3
# Second Digit is either 4 or 7
# <4 Digit> <6 Digit> <5 Digit>

lstCards = re.findall(r"3[4|7]\d{2}\s\d{6}\s\d{5}", empDetails)
print(lstCards)

# -----------------------------------------------------------------------------------

import re

sampleString = '''
Rohit made 122 runs, Virat made 96 runs, and
Dhawan made 46 runs and we won the match.
'''

# {"Rohit": 122, "Virat": 96, "Dhawan": 46}

lstName = re.findall(r"[A-Z][a-z]+", sampleString)
lstScores = re.findall(r"\d+", sampleString)

print(lstName)
print(lstScores)

result = {}
for index in range(3):
    result[lstName[index]] = lstScores[index]

print(result)

print(dict(zip(lstName, lstScores)))

# -----------------------------------------------------------------------------------

import re

s = "purple alice@google.com abcde helloab@abc.com ---@gmail.com abc_def@gmail.com 23@gmail.com my23@gmail.com"

emails = re.findall(r"\w+@\w+\.\w+", s)
print(emails)


emails = re.findall(r"[A-Za-z]\w+@\w+\.\w+", s)
print(emails)

# A-Za-z0-9_

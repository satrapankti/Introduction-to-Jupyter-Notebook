import datetime
import time

today = datetime.date.today()
print("Today: ", today)
print("Type of today: ", type(today))

currentTime = datetime.datetime.now()
print("Now: ", currentTime)
print("Type of currentTime: ", type(currentTime))

now = time.time()
print("Now using time module: ", now)

# EPOCH 1970 (Jan 1- 1970)

print("Today            : ", today)
print("Current Time     : ", currentTime)
print("Tuple format     : ", today.timetuple())
print("Ordinal          : ", today.toordinal())
print("Year             : ", today.year)
print("Month            : ", today.month)
print("Day              : ", today.day)

# -----------------------------------------------------------------------------------

import datetime

print("microseconds         : ", datetime.timedelta(microseconds=1))
print("milliseconds         : ", datetime.timedelta(milliseconds=1))
print("seconds              : ", datetime.timedelta(seconds=1))
print("minutes              : ", datetime.timedelta(minutes=1))
print("hours                : ", datetime.timedelta(hours=1))
print("days                 : ", datetime.timedelta(days=1))
print("weeks                : ", datetime.timedelta(weeks=1))


# today = datetime.date.today()
today = datetime.datetime.now()

print("Today                : ", today)

# delta = datetime.timedelta(days=1)
delta = datetime.timedelta(days=7, hours=4, minutes=10, seconds=40)

yday = today - delta
tom  = today + delta

print("Yesterday            : ", yday)
print("Tommorow             : ", tom)

print("Diff                 : ", tom - yday)

# -----------------------------------------------------------------------------------

import os

print(os.getcwd())

# os.mkdir("test")
if os.path.exists("test"):
    print("Directory already exists")
else:
    os.mkdir("test")

# Control + /

# -----------------------------------------------------------------------------------

import os

# os.system("notepad.exe")
prg = os.getcwd() + "\\Functions.py"
print("prg: ", prg)

os.system(prg)

# -----------------------------------------------------------------------------------

import os

print(os.listdir())
print(os.listdir(r"D:/"))

# SMTP
# SSH (paramiko)

# -----------------------------------------------------------------------------------

import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=’hostname’,username=’mokgadi’,password=’mypassword’)

# -------------------------------------------------------------------------------------------------------------

import subprocess

p1 = subprocess.Popen(["ping", "www.google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p1 = subprocess.Popen(["ping", "216.58.220.36"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(p1)
print(type(p1))

output = p1.communicate()[0]
print("Output: ", output)

error = p1.communicate()[1]
print("Error: ", error)

# --------------------------------------------------------------------------------------------------------------------------

import sys

print("System Platform              : ", sys.platform)
print("System Version               : ", sys.version)
print("System VerInfo               : ", sys.version_info)
print("Recursion Limit              : ", sys.getrecursionlimit())
print("Size of Int (Bytes)          : ", sys.getsizeof(10))
print("Size of List (Bytes)         : ", sys.getsizeof([]))
print("Size of Dict (Bytes)         : ", sys.getsizeof({}))
print("Windows Version              : ", sys.getwindowsversion())
print("System Path                  : ", sys.path)

# MAC Output
# System Platform              :  darwin
# System Version               :  3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)
# [Clang 6.0 (clang-600.0.57)]
# System VerInfo               :  sys.version_info(major=3, minor=9, micro=0, releaselevel='final', serial=0)
# Recursion Limit              :  1000
# Size of Int (Bytes)          :  28
# Size of List (Bytes)         :  56
# Size of Dict (Bytes)         :  64

# ------------------------------------------------------------------------------------------------------------------------------

import sys
# import somemodule
# from nsetools import Nse

# for index, item in enumerate(sys.path):
#     print(index, item)

# websites = ["amazon", "flipkart", "paytm"]
# for index, item in enumerate(websites):
#     print(index, item)

for item in sys.path:
    print(item)

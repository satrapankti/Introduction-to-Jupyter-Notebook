# w ==> Write Mode
# r ==> Read Mode
# a ==> Append Mode

#File Write

fh = open("FileExample.txt", "w")
print("File Handle: ", fh)
print("Type of fh : ", type(fh))

fh.write("Welcome to file handling in Python.\n")
fh.write("This is second line.\n")
fh.write("Always close the file once the job is done.\n")

fh.close()

# fh.write("Try writing after closing the file.\n") # Error, as the file is closed

# --------------------------------------------------------------------------------------------
#File Append

fh = open("FileExample.txt", "a")

fh.write("\n------------------------------------------\n")
fh.write("Testing append operations on file.\n")
fh.write("Done with append Operation.\n")

fh.close()

# -------------------------------------------------------------
#File Read

fh = open("FileExample.txt") # Default mode is read

strContents = fh.read()

fh.close()

print("File Content : ", strContents)
print("Type of strContents : ", type(strContents))

# ----------------------------------------------------------
# Pickle Read

import pickle

fh = open("TeamList", "rb") # rb ==> Read + binary

contents = pickle.load(fh)

fh.close()

print("Contents : ", contents)
print("Type of Contents : ", type(contents))

# Serialization - Deserialization
# Marshal - Unmarshal
# COM - DCOM

# ----------------------------------------------------------
# Pickle Write

import pickle

team = {
    "groupA": ["India", "NewZealand", "England"],
    "groupB": ["Aus", "WI", "SA"]
}

fh = open("TeamList", "wb") # wb => Write + Binary Mode
pickle.dump(team, fh)

fh.close()

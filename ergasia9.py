#ergasia9


f = open("asciifile.txt", "r")
print(f.read())
print("\n")

f = open("asciifile.txt", "r")
for line in f:
    for char in line:
        print("character " + char + " in ascii code is the numer: ", ord(char))
print("\n")

f = open("asciifile.txt", "r")
for line in f:
    for char in line:
        if(ord(char) % 2 == 1):
            print(char + " is odd in ascii code")

f = open("asciifile.txt", "r")
for line in f:
    for char1 in line:
        s=""
        for char2 in line:
            if(char1 is char2):
                s = s+ "*"
        print (char1 + " || " + s)

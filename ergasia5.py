#ergasia5
import random
import string

mikos = input("dose mikos: ")
platos = input("dose platos: ")

mikos = int(mikos)
platos = int(platos)
phrase = "so"
count = 0
row=""
column=""
diagonal=""

def statistics(column, row, diagonal):
    count = column.count("sos") + row.count("sos") + diagonal.count("sos")
    print (count/100)


for num in range(100):
    #dimiourgia listas kai arxikopoisi tis
    theList = [[random.choice(phrase) for x in range(mikos)] for x in range(platos)]

    #kanoume iteration stis stiles
    for j in range(mikos):
        for i in range(len(theList)):
            column = column+theList[i][j]

    #kanoume iteration stis grammes
    for i in range(len(theList)):
        for j in range(len(theList[i])):
                row = row+theList[i][j]

    #kanoume iteration stis diagonious
    for i in range(len(theList)):
        for j in range(len(theList[i])):
            if(i==j):
                diagonal = diagonal+theList[i][j]

statistics(column, row, diagonal)

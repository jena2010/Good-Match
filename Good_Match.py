#Graduate Assesment :Good Match
#Name : TINASHE JENA
import numpy as np
import csv

def calcPercentage(arr):
    temp = []
    reversed = arr.copy()[::-1]

    for i in range(int((len(arr)) / 2)):
        temp.append(arr[i] + reversed[i])
  
    if (len(arr) % 2 > 0):
        temp.append(arr[int((len(arr) - 1) / 2)])
        

    if (len(temp) == 2):
       
        if (len(str(temp[0])) == 2):
            arr = list(dict.fromkeys(list(str(temp[0]))))
            arr = list(map(int, arr))

            arr.append(temp[1])
            return calcPercentage(arr)
        elif (len(str(temp[1])) == 2):
           

            arr = [int(i) for i in str(temp[1])]
            arr = list(map(int, arr))

            arr.append(temp[0])
            arr = arr[::-1]
            return calcPercentage(arr)
        else:
            return temp
    
    else:
        return calcPercentage(temp)
  
def MatchResult():
    try:
        n1 = input(str("Enter 1st name"))
        n2 = input(str("Enter 2nd name"))
        InputMatch = matchPercentage(n1,n2)
        print(InputMatch)   
    except Exception as e:
        print("Invalid Input!! Please Enter only alphabetic characters",e)

    return InputMatch
    
MatchResult()
#Modify the program to accept as a CSV file input
def matchPercentage(name1, name2) :
    string = name1+" matches "+name2
    match = []
    number = []
    temp = list(string)
    temp = list(dict.fromkeys(temp))
    arr = np.array(temp)
    
    for i in range(len(string)):
        for j in range(len(string)):
            if (string[i] == string[j] and string[i] != " " and i != j):
                match.append(string[i])
      
    
    for char in arr:
        if (char in match):
            number.append(2)
        else :
            if (char != " ") :
                number.append(1)
    percentage = str(calcPercentage(number)[0])+""+str(calcPercentage(number)[1])
    if(int(percentage)>=80):
        comment = ", good match"
    
    else:
        comment = ""
    
    return string + " " + percentage + "%" + comment


males = []
females = []
with open('names.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        if(row[1] == 'm'):
            males.append(row[0])
        else:
            females.append(row[0])
males = list(dict.fromkeys(males))
females = list(dict.fromkeys(females))



for M  in males:
    for F in females:
        print(matchPercentage(M, F))
   

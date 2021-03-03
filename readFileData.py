#Script to import function from incrementNumber file
from incrementNumber import increment

#Function to read a file and get the last data insert
def getLastNumber(membre):
    if(membre == "GOV"):
        with open('GOV.txt') as file:
            for line in file:
                pass
            last_line = line
            increment(last_line, membre)
    elif(membre == "ORG"):
        with open('ORG.txt') as f:
            for line in f:
                pass
            last_line = line
            increment(last_line, membre)
    elif(membre == "COM"):
        with open('COM.txt') as f:
            for line in f:
                pass
            last_line = line
            increment(last_line, membre)
    else:
        print("Error this is not a membre class!")
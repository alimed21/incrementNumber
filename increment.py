#function that returns the last number generated for the membre class
def readFile(m):
    if (m == "GOV"):
        with open('GOV.txt') as f:
            for line in f:
                pass
            last_line = line
            increment(last_line, m)
    elif (m == "ORG"):
        with open('ORG.txt') as f:
            for line in f:
                pass
            last_line = line
            increment(last_line, m)
    elif (m == "COM"):
        with open('COM.txt') as f:
            for line in f:
                pass
            last_line = line
            increment(last_line, m)
    else:
        print("Error "+m+" this no a membre class!")

#function that generates the member code
def increment(s,m):
    out = ''
    number = ''
    NUMBERS = s
    for c in s:
        if c in NUMBERS:
            number += c
        else:
            if number != '':
                out += str(int(number) + 1)
                number = ''
            out += c

    if number != '':
        out += str(int(number) + 1)
        number = ''
        if (m == "GOV"):
            with open("GOV.txt", "a") as myFile:
                myFile.write("\n" + out)
            print("Done! this is the membre code : "+out)
        elif (m=="ORG"):
            with open("ORG.txt", "a") as myFile:
                myFile.write("\n" + out)
            print("Done! this is the membre code : "+out)
        else:
            with open("COM.txt", "a") as myFile:
                myFile.write("\n" + out)
            print("Done! this is the membre code : "+out)
    return out


#The main function
def main():
    membreClasse = raw_input('Enter your membre classe:')

    readFile(membreClasse)

if __name__ == "__main__":
    main()

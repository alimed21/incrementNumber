#Function to increment the last number insert into the file
def increment(s, m):
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
        with open('GOV.txt', 'a+') as myFile:
            myFile.write("\n"+out)
            print("Done! the membre code is : "+out)

    elif (m == "ORG"):
        with open('ORG.txt', 'a+') as myFile:
            myFile.write("\n" + out)
            print("Done! the membre code is : "+out)

    else:
        with open('COM.txt', 'a+') as myFile:
            myFile.write("\n" + out)
            print("Done! the membre code is : "+out)


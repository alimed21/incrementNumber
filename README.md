Algorithm which increments a number according to a type of member. By default I took 3 types of members, a number with 6 digits is assigned to it, The technology to use is Python3.

I have split the code into three functions:

the first function is the main (main function) iask the user to enter the member class then I call the second function, passing the user input as a parameter.


The second function checks the content of the variable. If the member class is correct then she will open the file that contains the member code and retrieve the last number  so that it passes as parameters to the three function.

Finally, the third function will have to configure the last number (member code) and the member class. It will check that the last incremented number is not NULL then increment it, once the number increment it checks the member class to insert this new number in the file of the member class and if this file does not exist it will create.

Allows you to open or create a file if it does not exist: **open("GOV.txt", "a")**

Allows you to write or insert data in a file: **myFile.write("\n" + out)**
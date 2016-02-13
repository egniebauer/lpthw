#opens system argv module (library)
from sys import argv

#names command-line argument variables
script, filename  = argv

#initializes variable "txt" to the function open with a parameter of
#	filename
txt = open(filename)

#prints text with the raw input format specifier for argv[1]
print "\nHere's your file %r:" % filename
# prints the file text using the read() function on the "txt" variable
print txt.read()

#requests input from the user
print "\nType the filename again:"
# initializes variable to user input
file_again = raw_input("> ")

#initializes variable to open function w/user input variable as the parameter
txt_again = open(file_again)

#prints the user's file text to the screen
print txt_again.read()

#closes the open files
txt.close()
txt_again.close()

print "\n"

#Exercise 17: More Files
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file); indata = in_file.read()

#print "\nThe input file is %d bytes long" % len(indata)

#print "\nDoes the output file exist? \n%r" % exists(to_file)
print "\nReady, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Complete.\n"

out_file.close()
in_file.close()

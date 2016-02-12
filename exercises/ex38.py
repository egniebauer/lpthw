# Exercise 38: Doing Things to Lists

# string variable
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 thing in that list. Let's first fix that."

# create 'stuff' list variable by executing the .split() method with a ' '
# parameter, on ten_things string variable - it will split the sting into
# separate strings at each ' '.
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:	# while the length of 'stuff' does not equal 10
	# create variable 'next_one' by running the .pop() method w/o any parameters
	# on the 'more_stuff' variable - it will "pop off" (remove) and return the 
	# last element the 'more_stuff' list.
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	
	# calls the append method with the parameter of 'next_one' variable on the
	# 'stuff' variable - it appends the passed object into the existing list
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

# prints index 1
print stuff[1]
# prints the last item of the list
print stuff[-1]
# prints the last item of the list after removing it from the list
print stuff.pop()
# prints string - the result of the .join() method being called on the ' '
# separator with the parameter of the 'stuff' list, which returns a string that
# has the elements of stuff concatenated with ' ' between ea.
print ' '.join(stuff)
# prints string - the result of the .join() method being called on the '#'
# separator with the parameter a slice the 'stuff' list, which returns a string
# from index 3 to 5 that have been concatenated by the '#' separator.
print '#'.join(stuff[3:5])

# Exercise 33: While Loops

# i = 0
# numbers = []
# 
# while i < 6:
# 	print "At the top i is %d" % i
# 	numbers.append(i)
# 	
# 	i += 1
# 	print "Numbers now: ", numbers
# 	print "At the bottom i is %d" % i
# 	
# 
# print "The numbers: "
# 
# for num in numbers:
# 	print num

# Study Drill
def list_func(max):
	max = int(max)
	list_numbers = []
	i = 0
	while i < max:
		print "At the top i is %d" % i
		list_numbers.append(i)
		i += 1
		print "Numbers now: ", list_numbers
		print "At the bottom i is %d" % i
	print "The numbers: "
	for num in list_numbers:
		print num

max_number = raw_input("Enter a number: ")
list_func(max_number)

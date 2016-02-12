# Exercise 39: Dictionaries, Oh Lovely Dictionaries

#Part 1
# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
	}

# create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
	}
# add some more cities by placing the key into the [] and setting the value
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", cities ['NY']
print "OR State has: ", cities ['OR']

# print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():	# .items() method returns a list of dict's 
									# (key, value) tuple pairs
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
# safely get an abbreviation by state that might not be there
# .get() method for key, returns value or default if key not in dictionary
# why not use .has_key() ?
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


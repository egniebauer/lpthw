# Exercise 36: Designing and Debugging
# Homework: Command-line Game

from sys import exit

def print_pet_list(num_pets):
	num_pets = int(num_pets)
	pet_list = []
	i = 0
	while i < num_pets:
		pet_list.append(i)
		i += 1
		print "%d good boy... " % i,
	
def hagrids():
	print """
	When you arrive at Hagrid's hut you find him and Fang
	are standing outside. Hagrid is happy to see you and
	smiles when you arrive. But you notice that he is also
	keeping a watchful eye on the Forbidden Forrest. Fang
	looks up at you and wags his tail. 
	
	Seeing them both makes you feel much better. 
	"""
	print "> 1. Pet Fang on the head."
	print "> 2. Ask Hagrid what's going on."
	choice = int(raw_input("\n> "))
	
	if choice == 1:
		print "\nHow many times?"
		fang_pets = int(raw_input("\n> "))
		
		if fang_pets < 5:
			print "\n"
			print_pet_list(fang_pets)
			print "\n\n\tFang grins widely."
			print "\n\tYou win the game!\n"
			exit(0)
		else:
			print "\tToo many pets! Fang can't control his excitement." 
			leave("You have drowned in dog drool")
	
	elif choice == 2:
		print "\n\tHagrid's looks at you happy and very serious:"
		print "\t\t\"\'s good to see yeh but this here \'s top secret."
		print "\t\tFer Dumbledore. Yeh understand. Bes\' be gettin\'"
		print "\t\tback ter the castle.\""
		harry()
	else:
		print "\nJust type a number!"
		hagrids()

def library():
	print """
	You're in the library.
	"""
	leave ("This option not built out yet.")

def malfoy():
	print """
	On your way to the quidditch field for practice you run
	into Malfoy with his usual rather large and rather dumb
	shadows, Crabbe and Goyle. Malfoy, standing behind the
	two brutes, who are now approaching you, wastes no time
	loudly taunting your from across the yard. Making sure you 
	can see his "POTTER STINKS" badge still blinking brightly.
	
	Obviously, you are in no mood for this. You...
	"""
	print "> 1. Turn and go back to the castle."
	print "> 2. Raise your wand at Crabbe and Goyle:"
	print '\t"Get out of my way you two!"'
	choice = int(raw_input("\n> "))
	
	brutes_moved = False
	while True:		
		if choice == 1 and not brutes_moved:
			print "\n\tYou've gone back to the castle."
			harry()
		elif choice == 2 and not brutes_moved:
			print "\n\tThey are easily intimidated and move out of your way.\n"
			brutes_moved = True
			print "> 1. Raise your wand to Malfoy:"
			print '\t"I hope you don\'t cower as easily as your fanboys!"'
			print "> 2. Get on your broom and fly away:"
			print '\t"Real tough guys you got there, Malfoy. See you losers later!"'
			choice = int(raw_input("\n> "))
			
		elif choice == 1 and brutes_moved:
			print "\n\tA dark and menacing voice comes from behind you:"
			print '\t\t"Potter!"'
			leave("Snape reports that you attacked Malfoy \"unprovoked\". You're expelled.")
		elif choice == 2 and brutes_moved:
				print "\n\tWhile flying, you see Hagrid's hut. You decide to visit."
				hagrids()
		else:
			print "\n\tJust type a number!"
			malfoy()

def crybaby():
	print """
	While your story is a sad one, you do have a lot of
	people who love and support you. Unfortunately, not
	one of them can help you now.
	
	While sulking... you receive an owl. Apparently, the
	Durselys became aware of your Gringotts fortune and,
	as your legal guardians, they withdrew the lot of your
	loot. Down to the last Knut.
	
	You can no longer fund your wizarding eduation.
	"""
	leave("You're heading back to 4 Privet Drive.")

def leave(why):
	print "\n\tGame over:", why, "\n\tGood job!\n"
	exit(0)

def harry():
	print "\n\tYou're now in Gryffindor Tower.\n"
	print "> 1. Whine a bit about how nobody cares."
	print "> 2. Practice your quidditch skills."
	print "> 3. Break the rules (but still get a zillion points for Gryffindor)."
	choice = int(raw_input("\n> "))
	
	if choice == 1:
		crybaby()
	elif choice == 2:
		malfoy()
	elif choice == 3:
		library()
	else:
		print "Just type a 1, 2, or 3 to make proceed."
		harry()
	
def start():
	print """
	You've just arrived back at Hogwarts. You know you should
	feel excited for the new school year ahead but you're still
	feeling a bit down from not receiving any birthday wishes
	over the summer holiday.
	"""
	character = raw_input("> Who are you?\n\n> ").lower()
	
	if "harry" in character or "potter" in character or "harry potter" in character:
		harry()
	elif "snape" in character:
		print "\n\t\"Well it may have escaped your notice,"
		print "\t but life isn't fair.\""
		print "\t\t-Professor Severus Snape"
		leave("You can't play with easter eggs!")
	else:
		print "\n\tWho? No. You're Harry Potter of course!"
		leave("Maybe the Dursleys were right about you.")

start()

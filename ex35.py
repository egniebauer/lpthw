# Exercise 35: Branches and Functions

from sys import exit

def gold_room():
	print "This room is full of gold. How many pieces do you take?"
	how_much = int(raw_input('> '))
	
	if how_much < 50:
		print "Nice, you're not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	choice = raw_input("> 'take honey' or 'taunt bear'\n> ")
	
	bear_moved = False
	while True:		
		if "take" in choice:
			dead("The bear looks at you then slaps your face off.")
		elif "taunt" in choice and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
			choice = raw_input("> 'open door' or 'taunt bear'\n> ")
		elif "taunt" in choice and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif "open" in choice and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever, stares at you and you go insane."
	print "Do you flee for your life or eat your own head?"
	choice = raw_input("> 'flee room' or 'eat head'\n> ")
	
	if "flee" in choice:
		start()
	elif "head" or "eat" in choice:
		dead("Well that was tasty.")
	else:
		cthulhu_room()

def dead(why):
	print "Game over:", why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your left and another to your right."
	print "Which one do you take?"
	choice = raw_input("> 'left' or 'right'\n> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()

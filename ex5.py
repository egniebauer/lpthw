# variable declaration
name = 'Elizabeth G. Niebauer'
age = 32			# nearly 33
ins = 65.0
cms = ins * 2.54
lbs = 140.0
kgs = lbs * 0.453592
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'


# program
print "Let's talk about %s." % name
print "She's %.0f inches tall." % ins
print "That's %.1f centimeters." % cms
print "She's %.0f pounds heavy (or %.1f kgs)." % (lbs, kgs)		# hey, I just had a baby!
print "Actually, that's not too heavy."						# exactly
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (age, ins, lbs, (age + ins + lbs))

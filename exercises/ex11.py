print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

#####

print '\nWhat\'s your name ?', 
name = raw_input('--> ')
print '\nHow old are you, %s?' % name,
age = int(raw_input())
print '\nHow tall are you (in cms), %s?' % name,
height = int(raw_input())
print '\nHow much do you weigh (in kgs), %s?' % name,
weight = int(raw_input())

print '\nSo, %s is %d years old, %d cms tall and weighs %d kgs.\n' %(
name, age, height, weight)

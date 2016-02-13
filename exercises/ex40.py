# Exercise 40: Modules, Classes, and Objects
from sys import exit

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rall around tha family",
						"With pockets full of shells"])

# happy_bday.sing_me_a_song()
# 
# bulls_on_parade.sing_me_a_song()

print '*' * 15


print "Would you like a song sung?"
ans = raw_input("'Y' or 'N'\n> ").lower()

if 'y' in ans:
	birthday_kid = raw_input('Who\'s birthday is it?\n> ')
		
	birthday_song = ["Happy birthday to you",
					"Happy birthday to you",
					"Happy birthday dear " + birthday_kid,
					"Happy birthday to you!"
					]
	
	birthday_song = Song(birthday_song)
	
	birthday_song.sing_me_a_song()
else:
	exit(0)

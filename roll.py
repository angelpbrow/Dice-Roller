from random import randrange

# roll a "die" some number of times.
# rolling die 3x
#result = ""

# roll - run it once and go into a loop

rolls = []

def die():
	roll1 = randrange(6)
	return rolls.append(roll1)

def die2():
	roll2 = randrange(6)
	return rolls.append(roll2)

def die3():
	roll3 = randrange(6)
	return rolls.append(roll3)


#i = 0
#def play():
#	while i <= 3:
#		if i == 1:
#			return die()
#		elif i == 2:
#			return die2()
#		else:
#			return die3()
#i += 1


die()
print(rolls)
die2()
print(rolls)
die3()
print(rolls)

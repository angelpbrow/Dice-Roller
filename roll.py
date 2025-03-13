from random import randrange

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


i = 0
def play():

    while (i <= 3):
        if (i == 1):
	         return die()
		elif (i == 2):
			return die2()
        else:
			return die3()
        i += 1

#die()
#die2()
#die3()
print(rolls)

from random import randrange

def dice(n):
	roll = randrange(1,7)

	print(roll)
	x = input ("would you like to roll again? Y/N?: ")
	while x == "Y":
		if (n == 1):
			dice(1)
		elif n == 2:
			rolls = []
			roll = randrange(1, 7)
			rolls.append(roll)
			roll2 = randrange(1, 7)
			rolls.append(roll2)
			print(rolls)
			break
		elif n == 3:
			rolls = []
			roll = randrange(1, 7)
			rolls.append(roll)
			roll2 = randrange(1, 7)
			rolls.append(roll2)
			roll3 = randrange(1, 7)
			rolls.append(roll3)
			print(rolls)
			break

dice(2)

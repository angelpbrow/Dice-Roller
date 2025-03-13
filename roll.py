from random import randrange

def die():
	roll = randrange(1,7)
	return roll

def game():
	play_game = True
	while True:
		rolls = []
		x = input("Your first roll is: " + randrange(1, 7))
		rolls.append(x)
		for i in range x:
			d = input("Your next roll is: " )
			rolls.append(d)
		p = input("Would you like to roll again?")
		if p == 'N':
			play_game = False


game()

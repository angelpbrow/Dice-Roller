from random import randrange

# roll a "die" some number of times.
# rolling die 3x
#result = ""

# roll - run it once and go into a loop



def die():
	roll = randrange(1,7)
	return roll

def game():
	play_game = True
while True:
	rolls[] = {}
	x = input("Your first roll is: " die())
	rolls.append(x)
for i in range int(x):
	d = input("Your next roll is: " + die())
	rolls.append(d)
p = input("Would you like to roll again?")
	if p == 'N':
		play_game = False

play_game()


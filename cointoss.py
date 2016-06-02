# Create a program that simulates coin toss. 


# need these two variables OUTSIDE function, or else re-writes every time
head = 0 
tail = 0 

for each in range(1, 11):
	import random
	# generates random number
	random_num = random.random()
	# rounds that random number to 0 or 1 
	rounded_random = round(random_num)

	if rounded_random == 1: 
		head += 1
		print "Attempt #", each, "Throwing coin.. It's Heads! Got", head, "heads so far!"
	else: 
		tail += 1
		print "Attempt #", each, "Throwing coin.. It's Tails! Got", tail, "tails so far!"

print "Ending program, thank you!"
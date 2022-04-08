import replit, time

def challenger():
	y=0
	t="Ben has challenged you to a fight!\n"
	while y <= len(t):
		replit.clear()
		print(t[:y])
		time.sleep(0.05)
		y = y + 1
	time.sleep(0.5)
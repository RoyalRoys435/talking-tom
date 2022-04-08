import random
import time
import replit
from begin import *
sleep = time.sleep




critchance = random.randint(0,10)
crit = 2

defended = random.randint(0,6)


def menub():
	print("Your Health: {}".format(hp))
	sleep(1)
	print("Enemy Health: {}".format(bosshp))
	sleep(1)
	print("\n[Attack] - Damages Ben.\n[Defend] - Chance to block Ben's attack.\n[Heal] - Regain some of your health.\n\n")

#attacks enemy
def attack():
	replit.clear()
	sleep(.2)
	print("You attack Ben. \n")
	critdmg = 1
	sleep(1)
	if critchance == 10:
		critdmg = damagedealt * crit
	print("You dealt {} damage.\n".format(damagedealt * crit))
	return damagedealt * crit
#
def defend():
	replit.clear()
	sleep(.2)
	print("You prepare your defences. \n")

def heal():
	replit.clear()
	sleep(.2)
	print("You wrap yourself in bandages. \n")
	sleep(1)
	print("You gained {} health. \n".format(plushp))

def battack():
	replit.clear()
	sleep(.2)
	print("Ben attacks you. \n")
	sleep(1)
	if prompt == "DEFEND":
			print("You deflected the attack. \n")
	else:
		print("You take {} damage. \n".format(damagetaken))

def bdefend():
	replit.clear()
	sleep(.2)
	if prompt == "ATTACK":
			print("Ben deflected your attack. \n")
	else:
		print("Ben tried to deflect you attack...\n")
		sleep(1)
		replit.clear()
		print("... but it failed")

def bheal():
	replit.clear()
	sleep(.2)
	print("Ben regained {} health. \n".format(plusbhp))

def mainfight():
	#main
	play = True
	hp = 20
	bosshp = 50
	challenger()
	while play == True:
		bturn = random.randint(1,6)
		defence = random.randint(0,3)
		damagedealt = random.randint(2,10)
		plushp = random.randint(5,12)
		plusbhp = random.randint(3,7)
		damagetaken = random.randint(1,8)
		if hp > 0 or bosshp > 0:
			if hp > 0:
				menub()
				prompt = input().upper()
			
				if prompt == "ATTACK":
					if bturn != 5:
						bosshp = bosshp - attack()
					sleep(1)
			
				elif prompt == "DEFEND":
					defend()
					sleep(1)
				elif prompt == "HEAL":
					replit.clear()
					heal()
					hp = hp + plushp
					if hp > 35:
						hp = 35
					sleep(1)
			else:
				break
		
			if bosshp > 0:
				if bturn < 5:
					battack()
					if prompt != "DEFEND":
						hp = hp - damagetaken
					sleep(1)
					replit.clear()
				elif bturn == 5:
					bdefend()
					sleep(1)
				elif bturn == 6:
					bheal()
					bosshp = bosshp + plusbhp
					if bosshp > 50:
						bosshp = 50
					sleep(1)
			else:
				break
		else:
			play = False
			break
	
	print("Your Health: {}".format(hp))
	print("Ben's Health: {}".format(bosshp))
	
	if bosshp <= 0:
		print("You Win!")
	elif hp <= 0:
		print("You Lose!")
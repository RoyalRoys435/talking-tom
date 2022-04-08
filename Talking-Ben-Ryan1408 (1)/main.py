"""
| updated by RoyalRoys435
"""

#made as a joke dont be a fucking bum... :)


#Talking ben's house in replit

import potions 
from potions import *
import random, replit, time
from replit import audio
from colorama import Fore
import boss
from boss import *
from begin import *
sleep = time.sleep
reply = ["'Yes'", "'No'"]
#RIP title
critchance = random.randint(0,10)
crit = 2

defended = random.randint(0,6)


def menub():
	print("Your Health: {}".format(hp))
	sleep(1)
	print("Enemy Health: {}".format(bosshp))
	sleep(1)
	print("\n[Attack] - Damages the enemy.\n[Defend] - Chance to block enemies attack.\n[Heal] - Regain some of your health.\n\n")

#attacks enemy
def attack():
	replit.clear()
	sleep(.2)
	print("You attack the enemy. \n")
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
	print("The Boss attacks you. \n")
	sleep(1)
	if prompt == "DEFEND":
			print("You deflected the attack. \n")
	else:
		print("You take {} damage. \n".format(damagetaken))

def bdefend():
	replit.clear()
	sleep(.2)
	if prompt == "ATTACK":
			print("The Boss deflected your attack. \n")
	else:
		print("The Boss tried to deflect you attack...\n")
		sleep(1)
		replit.clear()
		print("... but it failed")

def bheal():
	replit.clear()
	sleep(.2)
	print("The Boss regained {} health. \n".format(plusbhp))


#bens naughty pictures
def pic():
	print(Fore.WHITE + "		╖@╣╣╢▓╬@,╓╖╥╖∩╥╦╣╣╣╢▒▒╫╣╢╣▒▒▒▒╖\n        ▒╣▓▓╫╣╢╣▒╙▒▒▒╣▒║╣▒╣╣▒▒▒▒▒▒╢▓▓▓╣▒▒╓\n     ,╓║▓▓▓▓▓▓╣▒▒╢╫╣║╬╢╣╣▓▒▒▒▒▒▒▒▒░▒▓▓▓▓▓▒╗─\n     ▒▒╢▓▓▓▓▓▌░▒▒╫╣╢╫▒╢╢▒╢╢▓▓▓▓▓▓▓▒░▒▓▓▓▓╫╣▒[\n     ╢╫▓▓▓▓▓▓▒░▒╫╬▓▓▓▓▓▓▓▓▓▓███▌█▓▓▒▒▒▓█▓▓▓▓╬╣╖\n     ]╫╫▓▓▓▓▓▒▒╫▓▓▌▓████▓▓▓▓██▓▓▓▓▓╣╣╢▒▓█▓▓▓▓╢╣║╖\n    ,╫╣▓▓▓▓█▓▒╢╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢╢╣║╢▒▒▒▓█▓▓▓▓╬▓▒▒\n   ,╫╢▓▓▓▓▓█╣╢╢▒╢╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢╢▒▒▒▒▓██▓▓▓▓╫▒\n   ╟▓▓▓▓▓▒▒╜▒║╢╣▓╢▓▓██████████████▓▓╣▒▒▒@▒▒▓▓▓▓▓╢▒\n   ╫▓▓▓░░,▒╣║▒╢╫╫▓█████████████████▓▓▓╣▒▒▒▒░╙▀▓▓▓╣\n  ]╢▓▓▓∩░▒▒▒▒▒▓╣▓▓█████████████████▓▓▓▒╖,░░   ▒╜╙`\n  ║╫▓▓▓░░▒▒░▒▒▒▒▓▓▓████████████████▓▓▓╣▒░▒╓░░░▒\n '╨▓▓▓▓░▒▒▒▒▒▒▒▒╢╢▓▓╢███████████▓▓▓▓╣▒▒▒▒▒░░░▒▒\n      '╣╫╣▒▒▒▒▒░▒▒╫╫╫╫▓▓▓███▓▓╣▓▓▓▒╣▒╢Ñ▒▒▒▒▒▒▒\n       `╙╢╣▓▓▒▒▒╣▒╣╫▒▒╢▒╣▓▓▓▓╢╢▒▓▒╢▒▒▒▒╢▒╣▒Ñ░\n░          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣╣╣╢╬▒╢▒▒▒▒▒╫▓▓\n░░░░         ╙▓╢╣╣╫╫╣╣╢╢╣╢╢╢▓╣╬╣╬▓▓╣╣╢▓`\n░░░░░░░        ▒▓▓▓▓▓▓▒▒╢▒▒╢▒▒╢▒▒▓▓▓▓▓╣▓U,\n░░░░░░░      ,▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓╢╣╢╣╣╢╬@╖\n ░░░░░   ╔╦@▓▓▓▓▓▓▓▓▓▓╠▓╫▓▒╢▒╫╣║▒▒▒▒▒▒╣╢╢╣╣╬▒╬╖\n")
  

#menu
def menu():
  try: #errors fixed
    a = int(input(Fore.WHITE + "\n1 : Poke Ben \n2 : Talk to Ben \n3 : Call Ben\n4 : Tickle feet\n5 : Apple Juice\n6 : Beans\n7 : Burp\n8 : Lab\n9 : Credits\n10: 'Do you love God?'\n\nNumber: "))
    return a
  except ValueError:
    pass
    

#poke ben


def poke():
	replit.clear()
	r = random.randint(1,20)
	if r != 1:
		print("\nBen: Ooogghh\n\n" + Fore.RED + "*Ben is dissapointed*" + Fore.WHITE)
	else:
		print("\nBen: Ooohhff\n\n" + Fore.RED + "*Ben is almost dead you poked him too hard*" + Fore.WHITE)
		
def appleJuice():
	replit.clear()
	print("\nBen: *glug glug glug*\n\n" + Fore.LIGHTGREEN_EX + "*Ben really enjoyed that apple juice!*" + Fore.WHITE)

def beans():
	replit.clear()
	print(Fore.LIGHTGREEN_EX + "\n*Ben scoffs down the beans, delicious!*" + Fore.WHITE)

def burp():
	replit.clear()
	print("\nBen: *Burp*")

#talk to ben
def talk():
	replit.clear()
	s = str(input(Fore.LIGHTGREEN_EX + "\nBen is listening:  " + Fore.WHITE))
	print("\nBen: {}".format(s))



def credits():
  print (" _______________________________ \n|  ___________________________  |\n| | Ryan1408 + 22LMatt + HW556| |\n| |___________________________| |\n|_______________________________|")


#call ben
def call():
	replit.clear()
	calling = True
	print("\nBen: 'Bæn?'")
	try:
		audio.play_file("sound/Ben.wav")
	except:
		pass
	while calling == True:
		q = str(input("\nQuestion for Ben: "))
		hang = random.randint(0,14)
		
		
		if hang == 0:
			calling = False
			print(Fore.RED + "\n*Ben slammed the phone down*" + Fore.WHITE)

		elif q.lower() == "hang up":
			calling = False
			replit.clear()
			print(Fore.RED + "\n *Newspaper sounds*" + Fore.WHITE)

		else:
			print("\nBen:",reply[random.randint(0,3)])
					
#tickle feet
def feet():
	replit.clear()
	print("\nBen: Ooohh ;)\n\n" + Fore.LIGHTGREEN_EX + "*Ben likes that, he really likes that...*\n" + Fore.WHITE)

#lab
def lab():
  print(Fore.RED + "\n"+TheMotionOfThePotion() + Fore.WHITE) #pop fizz

  
#main
pic()
while 1 == 1:
	m = menu()
	if m == 1:
		poke()
	elif m == 2:
		talk()
	elif m == 3:
		call()
	elif m == 4:
		feet()
	elif m == 5:
		appleJuice()
	elif m == 6:
		beans()
	elif m == 7:
		burp()
	elif m == 8:
		lab()
	elif m == 9:
		credits()
	elif m == 10:
	#main
		play = True
		hp = 20
		bosshp = 100
		replit.clear()
		print("Hohoho...")
		time.sleep(1)
		replit.clear()
		print("No.")
		time.sleep(1)
		replit.clear()
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
		print("Enemy Health: {}".format(bosshp))
		
		if bosshp <= 0:
			print("You Win!")
		elif hp <= 0:
			print("You Lose!")
	else:
		print(Fore.RED + "No." + Fore.WHITE)
    
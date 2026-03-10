import random
from colorama import Fore,Back,Style,init
init(autoreset= True)
choices= ('rock','scissor','paper')
user_score= 0
computer_score= 0
print(Style.BRIGHT+Fore.BLUE+Style.BRIGHT+Back.WHITE+"     ROCK, PAPER, SCISSOR GAME      ")
while True :
	computer= random.choice(choices)
	user= input(Fore.CYAN+Style.BRIGHT+"Type ROCK, PAPER , SCISSOR and Q for quit==:"+Style.RESET_ALL).lower()
	print("Computer Chose=:", computer)
	if user== "q" :
		print(Style.BRIGHT+Fore.BLUE+"Thank You for giving us your precious time")
		break
	elif user== computer :
		print(Style.BRIGHT+Fore.RED+"Match Draw"+Style.RESET_ALL)
		print("Your Score=:", user_score)
		print("Computer Score=:", computer_score)
		continue
	elif user== "rock" and computer== "scissor" or user== "paper" and computer== "rock" or user== "scissor" and computer== "paper" :
		print(Style.BRIGHT+Fore.GREEN+"YOU WON"+Style.RESET_ALL)
		print(" Computer sended to you 🎉")
		user_score += 1
		print("Your Score=:", user_score)
		print("Computer Score=:", computer_score)
		
	elif user== "rock" and computer== "paper" or user==  "scissor" and computer== "rock" or user== "paper" and computer== "scissor" :
		print(Style.BRIGHT+Fore.YELLOW+"Computer Win 🤖")
		computer_score +=1
		print("Your Score=:", user_score)
		print("Computer Score=:", computer_score)
		argue= input(Style.BRIGHT+Fore.BLUE+"Do you want to send '🎉' to the computer. [Y] for Yes and [N] for no==:").upper()
		if argue== 'Y' :
			print(Style.BRIGHT+Fore.MAGENTA+"'🎉' Sended.")
			print(Style.BRIGHT+Fore.YELLOW+"Thank You (computer replied)")
		elif argue== "N" :
			pass 
	elif user not in choices :
		print(Fore.RED+Style.BRIGHT+"INVALID INPUT")
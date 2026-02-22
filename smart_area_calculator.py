from colorama import Fore, Back,Style, init
init(autoreset=True)

import getpass
print( Fore.RED + Back.WHITE + "	        SMART   AREA  CALCULATOR      ")
#--------retcangle-------#
#--------sqaure-----------#
#--------triangle-----------#
solid= input(Style.BRIGHT+Fore.CYAN+"TYPE THE SHAPE YOU WANT																		1). RECTANGLE 																														2). SQUARE																																3). TRIANGLE 																													==: "+Style.RESET_ALL)
if solid== "rectangle" or solid== "Rectangle" or solid== "RECTANGLE" :
	a= input("TYPE THE length(l)==:")
	b= input("TYPE THE breadth(b)==:")
	unit= input("TYPE THE UNIT(if you don't want to mention unit then click on the 'SPACE' button and then 'ENTER'' button ')==:")
	a= float(a)
	b= float(b)
	if unit== " " :
		print("The area of the rectangle will be==:", a * b,"unit square")
	else :
		print(" The area of the rectangle will be==:", a * b , unit,"square")
elif solid== "square" or solid== "SQUARE" or solid== "Square" :
	a= input("TYPE THE side==:")
	a= float(a)
	unit= input("TYPE THE UNIT(if you don't want to mention unit then click on the 'SPACE' button and then 'ENTER'' button ')==:")
	if unit== " " :
		print("The area of the rectangle will be==:", a * a , "unit square")
	else :
		print(" The area of the rectangle will be==:", a * a , unit,"square")
elif solid== "triangle" or solid== "TRIANGLE" or solid== "Triangle" :
	b= input("TYPE THE base of the triangle==:")
	h= input("TYPE THE height of the triangle==:")
	b= float(b)
	h= float(h)
	unit= input("TYPE THE UNIT(if you don't want to mention unit then click on the 'SPACE' button and then 'ENTER'' button ')==:")
	if unit== " " :
		print("The area of the triangle will be==:", b * h / 2 , "unit square")
	else :
		print("THE AREA OF THE TRIANGLE WILL BE", b * h / 2 , unit,"square")
else :
	print("SORRY THIS SOLID IS NOT PRESENT IN THE MENU")
print("----------THANK YOU----------")
#---------upgrade---------#
import sys
import random
import getpass
up= input(Fore.BLUE+Back.WHITE+"DO you want  to upgrade the app(yes/no) only 2 $ / month==:")

if  up== "YES" or up== "Yes" or up== "yes" :
	m= input("TYPE your bank account==: ")
	p= getpass.getpass("TYPE your password ==:")
	pn= input("TYPE the phone number linked with the bank account to recieve the otp==:")
	if pn.isdigit() and len(pn)== 10  :
		print(Style.BRIGHT+Fore.CYAN+Back.WHITE+"VALID No.")
	else :
		print(Style.BRIGHT+Fore.RED+Back.WHITE+"INVALID No.")
		sys.exit()
	otp= random.randint(10000,20000)
	
	print("------OTP----==:",otp)
	top= input("TYPE the otp sended on the number==:")
	top= int(top)
	if top== otp :
		print(Style.BRIGHT+Fore.GREEN+"CORRECT OTP")
		print(Style.BRIGHT+Fore.CYAN+Back.WHITE+"THANK YOU FOR UPGRADING THE APP")
		print(Style.BRIGHT+Fore.RED+"2$ has been debited from your account",m[:4],"*******")
		solid= input(Style.BRIGHT+Fore.BLUE+"Choose solid to obtain the perimeter:																1). RECTANGLE												2). SQUARE													3). TRIANGLE												==:")
		if solid== "rectangle" or solid== "RECTANGLE" or solid== "Rectangle" :
			length= input("TYPE THE LENGTH(l)==:")
			length= float(length)
			breadth= input("TYPE THE BREADTH(b)==:")
			unit= input("TYPE the unit")
			breadth= float(breadth)
			str= (length + breadth)
			str= float(str)
			print("The PERIMETER of the RECTANGLE is", 2 * str, unit)
		elif solid== "triangle" or solid== "TRIANGLE" or solid== "Triangle" :
			s= input("TYPE the side a ==:")
			a= input("TYPE the side b ==:")
			b= input("TYPE the side c ==:")
			unit= input("TYPE the unit==:")
			s= float(s)
			a= float(a)
			b= float(b)
			print("The perimeter of the TRIANGLE is", s + a + b, unit)
		elif solid== "square" or solid== "SQUARE" or solid== "Square" :
			s= input("TYPE the side of the square==:")
			unit= input("TYPE the unit")
			s= float(s)
			print("The perimeter of the triangle is", 4 * s, unit)
		else :
			print(Style.BRIGHT+Fore.RED+"This solid is not mentioned in the menu")
	elif top!= otp :
		print(Style.BRIGHT+Fore.RED+"INCORRECT OTP									PLEASE TRY AGAIN")
		sys.exit()
	else :
		pass
		
elif up== "NO" or  up== "No" or up== "no" :
	print(Style.BRIGHT+Fore.GREEN+"OK THANK YOU")
else :
	print(Style.BRIGHT+Fore.RED+"OOOOOPPPPPPSSSSS something went wrong")
	sys.exit()





#----------feedback-----------#
feed= input(Fore.MAGENTA+Back.WHITE+"DO YOU WANT TO GIVE US FEEDBACK(YES/NO)?==:")

if feed== "yes" or feed== "YES" or feed== "Yes" :
	feed= input("DO you want to give 'HIDDEN '  or 'SCREEN'(write) ")
	if feed== "hidden" or feed== "HIDDEN" or feed== "Hidden" :
		feed= getpass.getpass("How many stars do you want to give us (use these (*)to give us stars) ")
		if feed<= "**" :
			print(Style.BRIGHT+Fore.RED+"SORRY we will try our best next time")
		elif feed> "**" and feed< "*****" :
			print(Style.BRIGHT+Fore.GREEN+Back.WHITE+"THANK YOU ")
		elif feed>= "*****" :
			print("THANK YOU VERY MUCH for giving us your precious time")
		else :
			pass
	elif feed== "screen" or feed== "SCREEN" or feed== "Screen" :
		feed= input("How many stars do you want to give us (use these (*)to give us stars)==: ")
		
		if feed<= "**" :
			print(Style.BRIGHT+Fore.RED+"SORRY we will try our best next time")
		elif feed> "**" and feed< "*****" :
			print(Style.BRIGHT+Fore.GREEN+Back.WHITE+"THANK YOU ")
		elif feed>= "*****" :
			print("THANK YOU VERY MUCH for giving us your precious time")
		else :
			pass	
elif feed== "no" or feed== "NO" or feed== "No" :
	print("---THANK YOU for using the app--------																					-----VISIT AGAIN------")
else :
	print(Style.BRIGHT+Fore.RED+"ooopppppps 														something went wrong but , don't wory 																			Thank You for giving us your precious time")
	
print(Style.BRIGHT+Fore.CYAN+Back.WHITE+"------------THANK YOU-----------_")	
	
	
	

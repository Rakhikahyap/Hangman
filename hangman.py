import random
name=input("enter name")
print("______",name,"______")
print("******************")
print("_____welcome to the game hangman______")
print("-------------------------------------------------------------")
print("try to guess the word in less then 10 attemp")
def hangman():
	list=['shikha','lovely','himani','india','important','ritika']
	word=random.choice(list)
	turns=10
	guessmade=''
	letter=set('abcdefghijklmnopqrstuvwxyz')
	while len(word)>0:
		mainword=""
		missed=0
		for i in word:
			if i in guessmade:
				mainword=mainword+i
			else:
				mainword=mainword+"_ "
		if mainword==word:
			print(mainword)
			print("you won------")
			break
		print("guess a word",mainword)
		guess=input()
		if guess in letter:
			guessmade=guessmade+guess
		else:
			print("enter the valid charecters")
			guess=(input())
		if guess not in word:
			turns=turns-1
			if turns==9:
				print("9 turns are left")
				print("_____")
			if turns==8:
				print("8 turns are left")
				print("_____")
				print("         0          ")
			if turns==7:
				print("7 turns are left")
				print("_____")
				print("          0         ")
				print("          |         ")
			
			if turns==6:
				print("6 turns are left")
				print("_____")
				print("          0         ")
				print("          |         ")
				print("          /         ")
			if turns==5:
				print("5 turns are left")
				print("_____")
				print("          0         ")
				print("          |         ")
				print("         / \       ")
			if turns==4:
				print("4 turns are left")
				print("_____")
				print("         \0         ")
				print("          |         ")
				print("         / \       ")
			if turns==3:
				print("3 turns are left")
				print("_____")
				print("          \0/         ")
				print("           |         ")
				print("          / \         ")
			if turns==2:
				print("2 turns are left")
				print("_____")
				print("          \0/  |       ")
				print("           |         ")
				print("          / \         ")
			if turns==1:
				print("last turns are left")
				print("_____")
				print("          \0/_|       ")
				print("           |         ")
				print("          / \         ")
			if turns==0:
				print("you loose")
				print("yes let a good man die")
hangman()
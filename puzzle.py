import random

print('Crack the code! Have some fun ;)')



#Difficulty
length=int(input('\033[1;35;40mHow long do you want the word to be?\033[0;37m\n'))
tries=int(input('\033[1;35;40mIn how many tries do you think you can nail it?\033[0;37m\n'))


#Generate password
symbols=['B','R','G','Y']
word=''
for i in range(length):
	word+=random.choice(symbols)

WORD=list(word)
win='no'

lw=[0,0,0,0]


for i in WORD:
	if i=='B':
		lw[0]+=1
	if i=='R':
		lw[1]+=1
	if i=='G':
		lw[2]+=1
	if i=='Y':
		lw[3]+=1


#Playtime
for chance in range(tries):
	print('\033[1;35mType your guess as a '+str(length)+'-letter word from \"B,R,G,Y\" \033[1;31m('+str(tries-chance)+' tries remaining)')
	guess=str(input('\033[0;37m').upper())[0:length]
	chance+=1
	if guess==word:
		points=round(100*(1-chance*tries/length**3),2)
		if points>0:
			print('Hurray!! :D\nYou achieved a total of '+str(points)+' points')
		elif points<0:
			print('Found the word, still you managed to get a negative score of '+str(points)+'\nTry guessing a longer word with less tries, I know you are quite capable :D')
		else:
			print('Only a true master like yourself would be able to achive the \033[2;31mPERFECT ZERO SCORE\033[0;37m. I shall pay my due respects >,<')
		win='yes'
		break
	GUESS=list(guess)
	r=0	#right letters
	rr=0	#right letters in the right place

	lg=[0,0,0,0]

	for i in GUESS:
		if i=='B':
			lg[0]+=1
		if i=='R':
			lg[1]+=1
		if i=='G':
			lg[2]+=1
		if i=='Y':
			lg[3]+=1
	for i in range(4):
		if lg[i]==lw[i]:
			r+=lg[i]
		else:
			r+=min(lg[i],lw[i])

	for i in range(length):
		if GUESS[i]==WORD[i]:
			rr+=1
	print('Guessed '+str(r)+' of the letters with '+str(rr)+' of them in the right place\n\033[0;31m--------------------------------------------------------------------------')

if win=='no':
	points=round(10*length/tries,2)
	print('The answer was '+word+'\nKeep trying, I know you can do it. Got '+str(points)+' points for trying, though :)')

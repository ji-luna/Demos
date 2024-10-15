import random as rand

#RULES
numposs=4
possibilities=['B','R','G','Y']

print('Thank you for playing LETTER PUZZLE')
wordlen=int(input('How long do you want your word?\n'))
tries=10
word=[]
for i in range(wordlen):
    word.append(possibilities[rand.randint(0,3)])


status='pending'
for i in range(tries):
    print(str(tries-i)+' tries remain')
    guess=[letter for letter in input('Enter your guess\n').upper()]
    if guess==word:
        status='victory!!'
        break
    correct=0
    correct_order=0
    for poss in range(numposs):
        correct+=min(guess.count(possibilities[poss]),word.count(possibilities[poss]))
    for letter in range(wordlen):
        if guess[letter]==word[letter]:
            correct_order+=1
    print('You guessed '+str(correct)+' colors')
    print('You guessed '+str(correct_order)+' colors in the right place')
print(status)

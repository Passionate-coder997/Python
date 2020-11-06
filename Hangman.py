import random

print("\t\t\t\t\t\t\t\t Let's Play Hangman \n")
print("What's your Name?")
name=input()
print(f'\nHello {name} I am guessing of a continent if your guess matches with my guess then you will win the game.\n')

continents=('North America'.title(), 'South America'.title(), 'Europe'.title(), 'Asia'.title(), 'Africa'.title(), 'Antartica'.title(), 'Oceania'.title())

sec_word= random.choice(continents)

ln= 0
guess= 5

while guess > ln:
	c_i=input('Guess the name of a continent in the world: ').title()
	guess-=1
	print(f'Gusses Left: {guess}')
	if c_i==sec_word:
		print('Wooho!! You guessed it right')
		break
	elif c_i!=sec_word:
		print('Ohho!! Wrong guess')
else:
	print('You have lost the game')

	print(f'The correct word was {sec_word}')
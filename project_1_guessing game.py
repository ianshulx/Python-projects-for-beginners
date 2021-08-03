import random
number = random.randint(1, 100)

player_name = input("What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' guess a number between 1 and 100:')

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('YOU WIN ! ,You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('YOU LOOSE !, The number was ' + str(number))
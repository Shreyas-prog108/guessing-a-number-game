import random as r
print("Hii! What's your goodname?")
name=input()
print(f"Nice to meet you, {name},Let's Play a game")
print("I will think of a number between 1 to 10 and you have to guess it in less than 6 guesses")
num=r.randint(1,11)
guess_no=0
while(guess_no<6):
    print("Take a guess")
    guess=input()
    guess=int(guess)
    guess_no+=1
    if(guess<num):
        print("Ohh No!, You guessed a lower number")
    if(guess>num):
        print("Wrong!, guess a smaller number")
    if(guess==num):
        break;
if(guess==num):
    print("Yay Good job!", name , "You guessed number in", guess_no, "guesses")
if(guess!=num):
    print("Sorry the number I was think of was", num)
    print("You should try again")
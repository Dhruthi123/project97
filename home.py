import random
number=random.randint(1,9)
chances=0
print("guess a number between 1 to 9")

while chances<5:
    guess=int(input("enter your guess: "))
    if guess == number:
        print("congratulations you WON!!!")
        break
    elif guess<number:
        print("Your guess was too low , guess a higher number")
    else :
        print("your guess was too high , a lower number")


if not chances<5:
    print("YOU LOSE!!! the number is", number)
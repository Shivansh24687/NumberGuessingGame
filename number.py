import random 
number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9:")
while chances < 5:
    guess=int(input("Enter your guess:"))
    if guess==number:
        print("U won")
        break
    elif guess < number:
        print("Guess a higher number:")
    else:
        print("Guess a lower number:")
    chances+=1
if not chances < 5:
    print("U lose! The number is:",number)
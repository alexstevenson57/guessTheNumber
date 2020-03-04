import random


def randomNum():
    num = random.randint(1, 100)
    return num

def guess():
    points = 0
    randnum = randomNum()
    try:
        num = int(input("Please enter a number between 1 and 100: "))
    except ValueError:
        print("Please enter an integer")
        guess()
    if num < randnum:
        print("too low")
        points -= 5
    elif num > randnum:
        print("too high")
        points -= 5
    else:
        print("correct! first try!")
        points += 100
        ans = input("Would you like to play again? Yes or No: ")
        if ans == "Yes":
            guess()
        else:
            print("Your total points:", points)
            return
    i = 0
    while randnum != num:
        num = int(input("Please enter another number: "))
        if num < randnum:
            print("too low")
            points -= 5
        elif num > randnum:
            print("too high")
            points -= 5
        else:
            num = num
        i += 1
    print("correct!")
    points += 100
    ans = input("Would you like to play again? Yes or No: ")
    if ans == "Yes":
        guess()
    else:
        print("Your total points:", points)
        return

guess()
        
    
    

import random
print("_______________Welcome To my Number Guessing Game______________")
low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"---------YOU will Have 7 chances to Guess the Correct Number btwn {low} and {high}---------")
num = random.randint(low,high)
ch = 7
g=0

while g<ch:
    g+=1
    guess= int(input("Enter the Guess number: "))

    if guess == num:
        print("Hurrah!! You Guessed it Right!!")
        break
    elif guess < num:
        print(f"The number You Guessed is Low.....attempts left {ch-g}")
    else:
        print(f"The Number You Gussed is High.....attempts left {ch-g}")

if guess != num:
    print("Wrong Guess, You Are Out of Attempts!!")
    print(f"The Correct Number Was {num}")

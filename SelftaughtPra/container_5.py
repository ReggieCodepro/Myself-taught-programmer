color = {"purple", "orange", "green"}
guess = input("Guess a color:")

if guess in color:
    print("you guessed correctly!")
else:
    print("Wrong! Try again.")

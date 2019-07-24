
# CONDITIONALS

# Comparison Operators
# value1 == value2   "equal to"
# value1 > value2    "greater than"
# value1 < value2    "less than"
# value1 <= value2   "less than or equal to"
# value1 >= value2   "greater than or equal to"
# value1 != value2   "not equal to"

               ###

# if
likesAnime = True

if likesAnime == True:
    print("I like anime too!")

# "I like anime too!" will only be printed if likesAnime has a value of
# True.  Nothing will be printed if likesAnime is False.

               ###

# if-else
pet = "cat"

if pet == "cat":
    print("meow")
else:
    print("woof")

#  "meow" is printed if pet has a value of "cat".
#  "woof" will be printed if pet does not have a value of "cat".

               ###

# if-elif-else
secret_number = 8
user_input = input("Guess my secret number: ")
guess = int(user_input)

if guess > secret_number:
    print("The secret number is less than " + str(guess))
elif guess < secret_number:
    print("The secret number is greater than " + str(guess))
else:
    print("You guessed my secret number!")

# Note: You can have more than one elif

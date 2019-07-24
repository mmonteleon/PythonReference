# FUNCTION EXAMPLES

# Function Example 1

# DEFINING the function
def greet(name):
    return "Hello " + name + "!"
# name is a "parameter"
# It's a variable that will recieve the input to the function.

# CALLING the function
print(greet("Alex"))
# The input to a function is also called an argument.
# "Alex" is sent to the greet function as input.
# The output of this function call is "Hello Alex!"

               ###

# Function Example 2
# DEFINING the function
def calculate_tip(bill, percent):
    tip = bill * percent/100
    return tip

# CALLING the function
get_bill = input("How much did your meal cost? ")
get_percent = input("What percent would you like to tip? ")
bill = float(get_bill)
percent = float(get_percent)
tip = calculate_tip(bill, percent)
print("You should tip your server $" + str(tip))
# The inputs to the calculate_tip function are bill and percent.
# The output of the function is the tip.

               ###
# Function Example 3
# DEFINING the function
def name_game(name):
    print(name + "!")
    print(name + ", " + name + " bo-" + name)
    print("banana fana fo-" + name)
    print("fee fi mo-" + name)
    print(name + "!")
# This function is different from the others because it does not have
# a return value.  The output is a printed chorus of the name game.

# CALLING the function
name_game("Maria")
# Calling name_game with an input(argument) of "Maria" results in an output of:
# Maria!
# Maria, Maria bo-Maria
# banana fana fo-Maria
# fee fi mo-Maria
# Maria!

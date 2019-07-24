# DICTIONARY CRUD
# Create - How to create a new item in the data structure.
# Read - How to access an item in a data structure.
# Update - How to change an item in a data structure.
# Delete - How to remove an item from a list.

#####################################################
# Pikachu's name, Pokedex, height, weight, type
# Source: https://www.pokemon.com/us/pokedex/pikachu


pika_dict = {
    "name": "Pikachu",
    "pokedex index": 25,
    "height": "16 inches",
    "weight": "13.2 lbs",
    "type": "electric"
}

# Dictionaries have "key":"value" pairs
# The "name" key has a value of "Pikachu"
# The "pokedex index" has a value of 25
# Note: Dictionaries are created with "mustache" brackets

print(pika_dict)

### CREATE ###
pika_dict["category"] = "mouse"
pika_dict["ability"] = "static"

# Creating a new key:value pair in the dictionary using the following syntax:
# dict_name[key] = value

### READ ###
print(pika_dict["name"])
print(pika_dict["pokedex index"])

# Read information from the dictionary using this syntax:
# dict_name[key]

### UPDATE ###
pika_dict["name"] = "Pika"
print(pika_dict["name"])

pika_dict["height"] = "17 inches"
print(pika_dict["height"])

# Upadte values associated with a key using the "=" sign.  
# = is the assignment operator

### DELETE ###
del pika_dict["weight"]

# To delete key-value pairs use the del command.
# Syntax: del dict_name[key]


### ITERATING THROUGH A DICTIONARY ###
for item in pika_dict:
    print(item)
    
# This prints all of the keys in the dictionary

for key in pika_dict:
    print(pika_dict[key])
    
#This prints all of the values in the dictionary
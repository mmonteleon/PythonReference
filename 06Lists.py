# LISTS CRUD
# Create - How to create a new item in the data structure.
# Read - How to access an item in a data structure.
# Update - How to change an item in a data structure.
# Delete - How to remove an item from a list.

adventure_time_characters = ['Princess Bubblegum', 'Marceline', 'Lumpy Space Princess']

## CREATE ##
adventure_time_characters.append("Flame Princess")
# This adds the element "Flame Princess" at the end of the list.
# The list is now: ['Princess Bubblegum', 'Marceline', 'Lumpy Space Princess', 'Flame Princess']

adventure_time_characters.insert(2,"Tree Trunks")
# This inserts "Tree Trunks" at index 2.  
# All of the elements shift to accordingly.
# The list is now: ['Princess Bubblegum', 'Marceline', 'Tree Trunks', 'Lumpy Space Princess', 'Flame Princess']

adventure_time_characters.extend(["Finn", "Jake", "Lemongrab"])
# This extends the list with Finn, Jake, and Lemongrab
# The list is now: ['Princess Bubblegum', 'Marceline', 'Lumpy Space Princess', 'Flame Princess', 'Finn', 'Jake', 'Lemongrab']

## READ ##
print(adventure_time_characters[1])
#This prints "Marceline" since that is the element at index 1.

print(adventure_time_characters[2])
#This prints "Lumpy Space Princess" which is the element at index 2.

print("Printing the element at the end of the list")
print(adventure_time_characters[len(adventure_time_characters)-1])
# Remember, Python starts counting at zero.  The first element in the list has 
# an index of zero.  The second element has an index of one etc...
# The LAST ELEMENT will have an index of the length - 1.  So if a list has 5 
# items, the last index will be 4.  

## UPDATE ##
adventure_time_characters[2] = "BMO"
# This changes the element at index 2, from "Lumpy Space Princess" to "BMO"
# The list is now: ['Princess Bubblegum', 'Marceline', 'BMO', 'Flame Princess', 'Finn', 'Jake', 'Lemongrab']

## DELETE ##
adventure_time_characters.remove('Lemongrab')
# This removes "Lemongrab" from the adventure_time_characters list.
# The list is now:
# ['Princess Bubblegum', 'Marceline', 'BMO', 'Flame Princess', 'Finn', 'Jake']

adventure_time_characters.pop(4)
# This removes the element at index 4 ('Finn')
# The list is now:
# ['Princess Bubblegum', 'Marceline', 'BMO', 'Flame Princess', 'Jake']

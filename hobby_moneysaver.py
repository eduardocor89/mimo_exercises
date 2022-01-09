
hobbies = ["Archery", "Bolwing","Canoening","Dance","Embroidery","Flute","Gymnastics"]

# We're gonna cut down on the number of hobbies so let's shorten the list
# by running a while loop that'll do that for us. 

# while the last index of the hobbies list is not "dance"
while hobbies[-1] != "Dance":
    # delete the last index
    del hobbies[-1]

# We're going to count the number of hobbies I have 
# and assign them to a variable number. 

number = str(len(hobbies))
print("These are your " + number + " favorite hobbies:\n")
print(hobbies)
print()

extras = ["Gym","Cinema","Restaurants","Jewellery","Coffee","Netflix","Bingo"]
slashed = []

costs = [50,20,80,30,40,10,25]
to_save = 100
savings = 0

# we want to save 100 and while we have a positive value in that category, 
# we're gonna loop through the list until that value is 0.

# while the value of to save is greater than 0, perform these actions

while to_save >= 1:
    # look at the last index of costs and subtract that value from to_save
    # You're saving that money, so add it to the savings list.
    # Delete that last value since you're ready to go to the next one
    # Since the cost list and the extras list line up, you gotta keep things
    # parallel by deleting the last item from the extras list
    to_save -= costs[-1]
    savings += costs[-1]
    slashed.append(extras[-1])
    del costs[-1]
    del extras[-1]

# Convert this number into a string so you can use it. 
#       You can also type(convert) the variable inside of the method.
savings = savings
print("\nYou'll save $" + str(savings) + " by sticking to these extras:")
print(extras)
print()
print("These are the activities you stopped doing: " + str(slashed))

# If you need to save some more money, use this variable to store the next hobby
# you're likely to cut. 
next_saving = extras[-1]
print("\nIf you need to save more money, take some time off " + next_saving + " and ")
print("you could save $" + str(costs[-1]) + " more or $" 
    + str(savings + costs[-1]) + " in total.")





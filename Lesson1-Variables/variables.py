# Strings
myString = "Welcome to Electronic programing"
myStatus = "Time for "
myName = "Jamie"

print (myString)
print ("-----------------------")

# Numbers
myInteger = -42
myFloat = float(42)
print (myInteger)
# This will cause an error it is trying to join strings and numbers together.
# print ("Float: " + myFloat)
print ("Float: ", myFloat)
print (f'{myStatus} {abs(myInteger)}')
print ("-----------------------")

# Lists
icecream = ['Chocolate', 'Rum & Raisin', 'Hokey pokey'] # https://en.wikipedia.org/wiki/List_of_ice_cream_flavors
fibonacci = [1,2,3,5,8,13]

print (icecream)
print (icecream[1])
print (fibonacci[3])

icecream[0] = "Choc Chip"
print("Updated the 'Chocolate' entry to " + icecream[0])
fibonacci.append(21)
print (fibonacci)
print ("-----------------------")

# Dictionary (pairs of variables)

person =  {'Name': 'Jamie', 'Height': 186, 'Suburb': 'Jindalee'}
print (person['Suburb'] + " forever!")

print ("-----------------------")
print (myStatus + "'Pi'")
drinkTemp = 40
chillByC = 8
coolingAttempt = 0
drinkToHot = True

while drinkTemp > 10:
    print (f"Drink too hot to drink @ {drinkTemp}C")
    # Cool the beverage
    drinkTemp = drinkTemp - chillByC
    # Count how many times we have to chill the drink
    coolingAttempt = coolingAttempt + 1

print(f"Drink drink @ {drinkTemp}C after {coolingAttempt} chilling attempts")
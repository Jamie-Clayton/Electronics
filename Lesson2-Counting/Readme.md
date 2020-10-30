# Overview

- Recap Raspberry PI
- Recap variables
- Counting
- Storing data
- Introduction to sensors
- Introduction to displays
- Printing or CNC cases or mounts

## Counting

https://docs.python.org/3/tutorial/controlflow.html

Here is a simple counting example, where we change variables up or down be another number. The while loop allows us to keep doing a change until the drink temperature is greater than 10 degrees.

### While loops

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

### For loops


## Storing information

- Sensors will write output to files in the operating system
- You software programs will need to read those files
- Eventually you may want to store data, so you can recover it if your program stops or the power goes off. E.g. Weather data.

## Sensors

![Temperature](https://www.adeept.com/u_file/1706/products/30/0a78aa60da.jpg)

- RTFM! You have to configure your devices to receive data from sensors
  - Update operating system
  - Update your configuration to accept input
  - Trouble shooting (Google is your friend)

## Displays - Segment LED

![Segment LED](https://www.adeept.com/u_file/1706/products/30/94639c552d.jpg)

- OMG more binary code settings
- Stopping the program & display considerations

## From Prototype to Production

Considering what your going to do, when you want to 

- Cases/boxes/mounting
- Low form factors
- Mounting
- Power?
- Internet and security

## References

[Thingieverse - 3D printing ](https://www.thingiverse.com/)

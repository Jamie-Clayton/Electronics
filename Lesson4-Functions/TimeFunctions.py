import time
import asyncio


async def Clocks(switchOnTime, switchOffTime):
    print('Welcome')
    await time.sleep(switchOnTime)
    print('On')
    await time.sleep(switchOffTime)
    print('Goodbye')

def CountSheep(flock):

    return flock

await Clocks(5,10)
print (CountSheep(100))
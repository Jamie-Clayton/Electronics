import time

localtime = time.asctime(time.localtime(time.time()))
print ("Local current time :", localtime)

# Formate time with some of the structured data.
now = time.localtime()
print (f'{now.tm_hour}:{now.tm_min:02d}:{now.tm_sec:02d}')
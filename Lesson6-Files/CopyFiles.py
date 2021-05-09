# Copy files
from shutil import copyfile
import datetime

# Make a file date specific 
src = "WeatherData.log"
dst = "WeatherData-backup.log"
copyfile(src, dst)

src = "WeatherData.log"
today = datetime.date.today()
dst = "D:\RaspberryPi\WeatherData-" + str(today) + ".log"
copyfile(src, dst)
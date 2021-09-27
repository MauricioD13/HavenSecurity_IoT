import os
import glob
import time
import datetime
import RPi.GPIO as iO
import os,subprocess
from subprocess import call
from w1thermsensor import W1ThermSensor


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
# -------------------------------------
# Set a pointer to our W1thermsensor object,
# which will give us easy access to the sensor

mySensor = W1ThermSensor()

# -------------------------------------
# Print sensor values
while True:
  try:
    for mySensor in W1ThermSensor.get_available_sensors():
      curSensorID = mySensor.id
      curTemp = mySensor.get_temperature()
      curTemp = round(curTemp,1)
      print(f"temp: {curTemp}")
      myTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d@%H:%M:%S")		
      print(curSensorID + " Temp = " + str(curTemp) + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")) 
  except:
    pass

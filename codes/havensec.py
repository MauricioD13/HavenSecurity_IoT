import tempmqtt
import rfcamdrop

import ventilador
from time import time, sleep
import RPi.GPIO as GPIO
from threading import Thread  
import signal

time_vent = time()
time_temp = time()
time_rf = time()

def signal_handler(signum, frame):
    """ Function for signal call
    """
    print("***Vent***")
    ventilador.vent_func()
    print("***Temp y Gas***")
    tempmqtt.temp_mqtt_func()
    signal.alarm(5)


""" Signal library config"""

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(5)


""" Modules config """

ventilador.vent_config()
dbc, reader = rfcamdrop.rfid_dropbox_config()

while True:
        print("***RFID***")    
        rfcamdrop.rfid_dropbox_func(dbc, reader)

    



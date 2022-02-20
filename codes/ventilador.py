import time
import json
import requests
import RPi.GPIO as GPIO
import os


def vent_config():
    channel_ID_write = "" 
    channel_ID_read = "1509577" #Id unico del canal extraido de Thingspeak
    mqtt_host = "mqtt3.thingspeak.com" #Nombre del host de teamspeak

    mqtt_client_ID = "JhgWCisEHiwuOCgqLBsDCiA" #Id del cliente unico para el topic
    mqtt_username = os.environ['USER_THINGSPEAK'] #Username unico de Thingspeak
    mqtt_password = os.environ['PASS_THINGSPEAK'] #Contraseña unica Thingspeak

    t_transport = "websockets" #Metodo comunicacion
    t_port = 80 #Puerto para la comunicacion

    topic = "channels/" + channel_ID_read + "/publish" #El topic se contruye en base al ID de canal unico
    
    vent_pin = 12

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(vent_pin,GPIO.OUT)
    
    GPIO.output(vent_pin,GPIO.LOW)


def vent_func():

    get_data = requests.get('https://api.thingspeak.com/channels/1509577/fields/4.json?results=2').json()
    
    vent_pin = 12
    GPIO.output(vent_pin, GPIO.LOW)

    cha_ID = get_data['channel']['id']
    lect = get_data['feeds']
    t=[]

    for x in lect:
        vent_act = x['field4']
        t.append(x['field4'])

    print(get_data)
    print(cha_ID)
    print(t)
    print(vent_act)
    
    if vent_act == None:
        vent_act = 0
        


    if int(vent_act):
        GPIO.output(vent_pin, GPIO.HIGH)
    else:    
        GPIO.output(vent_pin, GPIO.LOW)

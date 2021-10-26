import time
import json
import urllib.request
import requests
import RPi.GPIO as GPIO

channel_ID_write = "" 
channel_ID_read = "1509577" #Id unico del canal extraido de Thingspeak
mqtt_host = "mqtt3.thingspeak.com" #Nombre del host de teamspeak

mqtt_client_ID = "JhgWCisEHiwuOCgqLBsDCiA" #Id del cliente unico para el topic
mqtt_username = "JhgWCisEHiwuOCgqLBsDCiA" #Username unico de Thingspeak
mqtt_password = "6P6FHOXeuh2SUFmrirNj7sLU" #Contraseña unica Thingspeak

t_transport = "websockets" #Metodo comunicacion
t_port = 80 #Puerto para la comunicacion

topic = "channels/" + channel_ID_read + "/publish" #El topic se contruye en base al ID de canal unico

vent_pin = 12



GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(vent_pin,GPIO.OUT)

#payload = "field1=" + str(curTemp) + "&field2=" + str(curGas) + "&field3=" + str(myTimeStamp) # "2021-12-12-10:10" #Se construye el payload con los datos del sensor de temperatura y sensor de gas
#print("Escribiendo mensaje=", payload, "al host: ", mqtt_host, "clientID= ", mqtt_client_ID)
        
#publish.single(topic, payload, hostname=mqtt_host, transport =t_transport, port =t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username, 'password':mqtt_password})#Se publica la informacion del payload hacia el servidor Thingspeak

get_data = requests.get('https://api.thingspeak.com/channels/1509577/fields/4.json?results=2').json()

cha_ID = get_data['channel']['id']
lect = get_data['feeds']
t=[]

for x in lect:
    vent_act = x['field4']
    t.append(x['field4'])


print(cha_ID)
print(t)
print(vent_act)


if vent_act:
    GPIO.output(vent_pin, GPIO.HIGH)
    time.sleep(15)
    GPIO.output(vent_pin, GPIO.LOW)


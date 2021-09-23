import paho.mqtt.publish as publish
import string 
import time
import smbus
import sys

"""Se necesita descargar la libreria de mqtt primero, hay de Python normal y python3"""
"""Incluir Time stamp y un ID para cada sensor"""

channel_ID = "1509577"
mqtt_host = "mqtt3.thingspeak.com"

mqtt_client_ID = "JhgWCisEHiwuOCgqLBsDCiA"
mqtt_username = "JhgWCisEHiwuOCgqLBsDCiA" 
mqtt_password = "6P6FHOXeuh2SUFmrirNj7sLU"

t_transport = "websockets"
t_port = 80

topic = "channels/" + channel_ID + "/publish" #+ apiKey

while(True):

    cpu_percent = 1 #psutil.cpu_percent(interval= 20)
    ram_percent = 2 #psutil.virtual_memory().percent

    payload = "field1=" + str(cpu_percent) + "&field2=" + str(ram_percent)
    
    if cpu_percent == 10 :
        cpu_percent = 1
        ram_percent = 2

    cpu_percent +=1
    ram_percent +=2

    try:
        print("Escribiendo mensaje=", payload, "al host: ", mqtt_host, "clientID= ", mqtt_client_ID)
        
        publish.single(topic, payload, hostname=mqtt_host, transport =t_transport, port =t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username, 'password':mqtt_password})
    
    except (KeyboardInterrupt):
        break
    
    except Exception as e:
        print(e)




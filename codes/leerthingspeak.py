import json
import network
import urequests
import wlan

wlan.do_connect()

consulta = urequests.get("https://thingspeak.com/channels/548625/feeds.json?results=2")
data = consulta.json()

temp = data["feeds"][0]["field1"]

print("Temperatura: ",temp)

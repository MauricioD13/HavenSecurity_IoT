import paho.mqtt.publish as publish
from time import sleep
import smbus
import sys

channelID = "1509577"

apiKey = "MT0JJEJYRP9MXT7X"

useUnsecuredTCP = True

useUnsecuredWebsockets = False

useSSLWebsockets = False

mqttHost = "mqtt:// mqtt3.thingspeak.com"

if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443

topic = "channels/" + channelID + "/publish/" + apiKey

i=1

while (True):

    tPayload = "prueba thingspeak:" +str(i)

    i=i+1
 
    if i == 10:
        i=1

    try:
        mqtt_auth = None
        if len(mqtt_username) > 0:
            mqtt_auth = {'username':"JhgWCisEHiwuOCgqLBsDCiA", 'password': "6P6FHOXeuh2SUFmrirNj7sLU" }
        publish.single(topic, payload=tPayload, qos=0, retain=False, hostname=mqttHost, port=tPort, client_id="JhgWCisEHiwuOCgqLBsDCiA", keepalive=60, will=None, auth=mqtt_auth, tls=tTLS, transport=tTransport)
        time.sleep(1)

    except (KeyboardInterrupt):
        break

    except:
        print("Hubo un error imprimiendose los datos")

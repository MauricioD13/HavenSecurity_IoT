#! /usr/bin/python3
from time import sleep
from mfrc522 import SimpleMFRC522
import os
import dropbox
import RPi.GPIO as GPIO
import signal



"""Dropbox, spidev, mfrc522, signal"""

continue_reading = True

print ("Asegurado por Haven Security")

print ("Presione Ctrl-C para parar.")

# Capturar la señal para acabar la leida de tarjeta
def end_read(signal,frame):
    global continue_reading
    print ("Cerrando sistema")
    continue_reading = False
    GPIO.cleanup()
    

# Captura el SIGINT
signal.signal(signal.SIGINT, end_read)

reader = SimpleMFRC522() #Se crea un objeto MFRC522 llamado reader

dbc = dropbox.Dropbox('VEC5BwdnK3oAAAAAAAAAAbYRIpkZoWvNRF_1H5DQVtFJ886LCtwFu2iWOTVDT19u')
#print('Informacion de cuenta:', dbc.users_get_current_account())

# Nombre de la imagen 
i = 1

# Este loop busca la tarjeta 
while continue_reading:
    
    id, text= reader.read()
    print(id)
    #print(text)

    if 151019198817 == id:
        print("Tarjeta identificada")
        fname = 'imagen' + '_' +str(i)+'.jpg'
        fpath = '/home/pi/Desktop/rfidpy3/'+fname
        comando="raspistill -o "+str(fname)
        os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
        i+=1
        f=open(fname,'rb')
        res=dbc.files_upload(f.read(),fpath, mute =True)
        print("Resultado: ",res)
        #print(dbc.files_get_metadata(fpath).server_modified)
        dbc.close()

    if 533916563683 == id:
        print("Tag identificada")
        fname = 'imagen' + '_' +str(i)+'.jpg'
        fpath = '/home/pi/Desktop/rfidpy3/'+fname
        comando="raspistill -o "+str(fname)
        os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
        i+=1
        f=open(fname,'rb')
        res=dbc.files_upload(f.read(),fpath, mute =True)
        print("Resultado: ",res)
        #print(dbc.files_get_metadata(fpath).server_modified)
        dbc.close()


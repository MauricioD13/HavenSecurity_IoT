#! /usr/bin/python3
from time import sleep
from mfrc522 import SimpleMFRC522 #Libreria para el manejo del sensor rfid
import os #Libreria para el manejo de comandos del sistema
import dropbox #Libreria para dropbox
import RPi.GPIO as GPIO
import signal #Libreria para capturar la interrupcion del teclado

"""Dropbox, spidev, mfrc522, signal"""

continue_reading = True

print ("Asegurado por Haven Security")

print ("Presione Ctrl-C para salir.")

# Capturar la señal para acabar la leida de tarjeta
def end_read(signal,frame):
    global continue_reading
    print ("Cerrando sistema")
    continue_reading = False
    GPIO.cleanup()
    

# Captura el SIGINT
signal.signal(signal.SIGINT, end_read)

reader = SimpleMFRC522() #Se crea un objeto MFRC522 llamado reader

dbc = dropbox.Dropbox('_rqxShCd_6YAAAAAAAAAAaeOv4CbWaoQBGlynuE_YnZ55GZVqu-vHehGNKxiCzF9')#Token de autorizacion 

print('Informacion de cuenta:', dbc.users_get_current_account())

# Nombre de la imagen 
i = 1

# Este loop busca la tarjeta 
while continue_reading:
    
    id, text= reader.read() #Funcion que lee el ID de la tarjeta y el texto en caso de que se transmita alguno
    print(id)
    #print(text)

    if 151019198817 == id: #Si es el de la tarjeta
        print("Tarjeta identificada")
        fname = 'imagen' + '_' +str(i)+'.jpg'  #Se contruye el nombre de la foto a tomar
        fpath = '/home/pi/HavenSecurity_IoT/codes/'+fname #El path donde se guarda la foto
        comando="raspistill -o "+str(fname) #Se construye el nombre de la foto
        os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
        i+=1
        f=open(fname,'rb') #Abre el archivo para ser enviado
        res=dbc.files_upload(f.read(),fpath, mute =True) #Se envia el archivo 
        print("Resultado: ",res) #Se muestra el resultado del envio
        #print(dbc.files_get_metadata(fpath).server_modified)
        dbc.close()

    if 533916563683 == id: #Si el id es el del tag
        print("Tag identificado")
        fname = 'imagen' + '_' +str(i)+'.jpg'
        fpath = '/home/pi/HavenSecurity_IoT/codes/'+fname
        comando="raspistill -o "+str(fname)
        os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
        i+=1
        f=open(fname,'rb')
        res=dbc.files_upload(f.read(),fpath, mute =True)
        print("Resultado: ",res)
        #print(dbc.files_get_metadata(fpath).server_modified)
        dbc.close()


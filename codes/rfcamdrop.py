#! /usr/bin/python3
from time import sleep
from mfrc522 import SimpleMFRC522 #Libreria para el manejo del sensor rfid
import os #Libreria para el manejo de comandos del sistema
import dropbox #Libreria para dropbox
import RPi.GPIO as GPIO
import signal #Libreria para capturar la interrupcion del teclado
import multiprocessing as mp

def rfid_dropbox_config():
    """ RFID sensor config 
        Dropbox config
    """
    print ("Asegurado por Haven Security")

    print ("Presione Ctrl-C para salir.")

    # Capturar la señal para acabar la leida de tarjeta

    reader = SimpleMFRC522() #Se crea un objeto MFRC522 llamado reader

    dbc = dropbox.Dropbox('KxL2v9KtxYwAAAAAAAAAAblg3U4IVJ9YS8iNJI2yowo9o6jv9l-6hVggIyRS49eq')#Token de autorizacion 

    return dbc, reader


def rfid_dropbox_func(dbc, reader):
    """ Read card
        Take photo
        Upload to dropbox directory
    """
    id, text= reader.read() #Funcion que lee el ID de la tarjeta y el texto en caso de que se transmita alguno
    print("id: ", id)
    
    # Allowed ID's
    ids = {
            1:151019198817,
            2:533916563683,
            3:36706355413,            
        }

    # Iterate for all values and keys in the dict 
    for key,value in ids.items():
        if id==value: #Si es el de la tarjeta
            print("Tarjeta identificada")
            fname = 'imagen' + '_' +str(value)+'_'+'.jpg'  #Se contruye el nombre de la foto a tomar
            fpath = '/home/pi/HavenSecurity_IoT/codes/'+fname #El path donde se guarda la foto
            comando="raspistill -o "+str(fname) #Se construye el nombre de la foto
            os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
        
            f= open(fname,'rb')#Abre el archivo para ser enviado
    
            res = dbc.files_upload(f.read(),fpath, mute =True, mode=dropbox.files.WriteMode.overwrite ) #Se envia el archivo 
            print("Resultado: ", res) #Se muestra el resultado del envio
        
            dbc.close()
        


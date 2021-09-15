#!/usr/bin/env python
# -*- coding: utf8 -*-
#


import RPi.GPIO as GPIO
import MFRC522
import signal
import os

continue_reading = True

# Capturar la señal para acabar la leida de tarjeta
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Captura el SIGINT
signal.signal(signal.SIGINT, end_read)

# Crear objeto de la clase MFRC522
MIFAREReader = MFRC522.MFRC522()

# Mensaje de bienvenida
print ("Asegurado por Haven Security")
print ("Presione Ctrl-C para parar.")

# Nombre de la imagen 
i = 1

# Este loop busca la tarjeta 
while continue_reading:
    
    # Escanea por tarjetas   
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Si se detecta una tarjeta
    if status == MIFAREReader.MI_OK:
        print ("Tarjeta detectada")
    
    # Obtiene la  UID de la tarjeta
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Si se tiene UID, que continue
    if status == MIFAREReader.MI_OK:

        # Imprimir UID
        #print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    
        # Llave default para autenticar
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Seleccionar la tag scaneada
        MIFAREReader.MFRC522_SelectTag(uid)

        # Autenticar
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Verificar la autenticacion
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
            name = 'imagen' + '_' +str(i)+'.jpg'
            comando="raspistill -o "+str(name)
            os.system(comando) # Cuando la tarjeta sea identificada que tome la foto
            i+=1
            
        else:
            print ("Error de autenticacion")


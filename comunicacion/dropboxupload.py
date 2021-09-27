#! /usr/bin/python3
from time import sleep
import os
import dropbox

"""Se debe instalar la libreria Dropbox para python3"""

comando="raspistill -o "+"image.jpg"
sleep(1)
os.system(comando)
sleep(1)

dbc = dropbox.Dropbox('sl.A46GLr0vuBjmMPleQnxys4YO4EHYvnx1aFgVXAJhLLZpA3-3HGbjztTXAZR5IxT80pPKkfcTNhyL8lfM3WrFWn3bifC3nHyaeX3Nxn6byuNMcl283Tiw_D5OHClztootLSf9gi7A')
print('Informacion de cuenta:', dbc.users_get_current_account())

fname="image.jpg"
f=open(fname,'rb')
res=dbc.files_upload(f.read(),'/home/pi/comunicacion/image.jpg', mute =True)
print("Resultado: ",res)
#print(dbc.files_get_metadata('/home/pi/comunicacion/image.jpg').server_modified)
dbc.close()


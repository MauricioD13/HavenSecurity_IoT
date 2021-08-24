import socket
import threading #Usar varios hilos en un mismo programa, para que el servidor pueda atender varios pedidos
import queue
import time

queue_menu = queue.Queue()
HEADER = 64

PORT = 7000

SERVER = socket.gethostbyname(socket.gethostname()) #gethostname devuelve el nombre del pc en que se esta corriendo el script
#gethostbyname sabiendo cual es el nombre de la maquina esta funcion devuelve la direccion de IP del pc

FORMAT = 'utf-8' #Formato para la conversion del mensaje recibido
DISCONNECT_MESSAGE="!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#El primer parametro es la familia del protocolo qeu se va a estudiar
#El segundo parametro indica que los datos seran enviados de manera stream
    #tambien hace referencia a una conexion TCP/IP
ADDR =(SERVER,PORT) #Debe ser una tupla para usar el socket

server.bind(ADDR)# Se une el socket a la direccion del pc

def start(): #Nuevas conexiones
    
    server.listen() #Escuchar para nuevas conexiones
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    conn, addr=server.accept()
    conn.sendall(b'Hola')
    
    #El metodo accept() devuelve la direccion donde esta el socket del cliente y tambien el objeto, i.e, el socket
    print(f"Direccion cliente IP: {addr}")
    return conn
def receive_info(conn):
    msg = conn.recv(1024)
    print(msg)    
    

print("[STARTING] server is starting...")
conn = start()
while True:
    receive_info(conn)
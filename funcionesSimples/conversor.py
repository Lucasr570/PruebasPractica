import os
clear = lambda: os.system('cls')
clear()

#Creamos la funcion menu
def menu():
    print('\nMenu')
    print("1. Dolar")
    print("2. Euro")
    print("3. Real")
    print("4. Libra")
    print("5. Franco")
    global pesos
    pesos = float(input('\nCuanto tienes en pesos?_ '))
    global cambio
    cambio = int(input('Que tipo de cambio deseas realizar?_ '))
    
#Evaluamos el tipo de cambio
    if (cambio == 1):
        dolares()
    elif (cambio == 2):
        euro()
    elif (cambio == 3):
        real()
    elif (cambio == 4):
        libra()
    elif (cambio == 5):
        franco()
    else:
        print('El tipo de cambio que seleccionaste no existe')
        
    global respuesta
    respuesta = input('Deseas hacer otra conversion? ( si/no ')
    respuesta = respuesta.lower()
    repetir()
    
def dolares():
    global precioD
    precioD = float(input('Cual es el precio del dolar el dia de hoy?_'))
    global convRealizada
    convRealizada = pesos/precioD
    print('Tienes ', convRealizada, 'Dolares')
    
def euro():
    global precioE
    precioE = float(input('Cual es el precio del eeuro el dia de hoy?_'))
    global convRealizada
    convRealizada = pesos/precioE
    print('Tienes ', convRealizada, 'Euros')
    
def real():
    global precioR
    precioR = float(input('Cual es el precio del real el dia de hoy?_'))
    global convRealizada
    convRealizada = pesos/precioR
    print('Tienes ', convRealizada, 'reales')
    
def libra():
    global precioL
    precioL = float(input('Cual es el precio de la libra el dia de hoy?_'))
    global convRealizada
    convRealizada = pesos/precioL
    print('Tienes ', convRealizada, 'Libras')
    
def franco():
    global precioF
    precioF = float(input('Cual es el precio del franco el dia de hoy?_'))
    global convRealizada
    convRealizada = pesos/precioF
    print('Tienes ', convRealizada, 'francos')
    
def repetir():
    while (respuesta != 'no'):
        menu()
 
 
 #Llamando a la funcion menu   
menu()
from email.mime import audio
import pytube
import os
clear = lambda: os.system('cls')
clear()

print("BIENVENIDO AL SISTEMA DE DESCARGA DE YOUTUBE")

url = input("Ingrese la URL completa del video: ")
yt = pytube.YouTube(url)

def descarga(error):
    print("")
    if(error):
        print("Opción no valida")
        
    print("ELIJA LA OPCIOÓN DESADA: ")
    print("1 - Video alta Definicion")
    print("2 - Video Baja definición")
    print("3 - Solo Audio mp3")
    opt = input()
    
    if(opt == "1"):
        print("DESCARGANDO... aguarde")
        video = yt.streams.get_highest_resolution()
        video.download(filename='temporal.mp4')
    elif(opt == "2"):
        print("DESCARGANDO... aguarde")
        video = yt.streams.get_lowest_resolution()
        video.download(filename='temporal.mp4')
    elif(opt == "3"):
        print("DESCARGANDO... aguarde")
        audio = yt.streams.get_audio_only()  
        audio.download(filename='temporal.mp3')
    else:
        print("Opción no válida")
        descarga(True)
        
        
descarga(False)
print("DESCARGA COMPLETA")
 
        
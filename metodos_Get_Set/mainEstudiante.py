from EstudianteClass import *
import os
clear = lambda : os.system('cls')
clear()

estudiante = None

while True:
    
    print("\n\n MENU \n")
    print("1. AGREGAR ESTUDIANTE")
    print("2. MODIFICAR DATOS")
    print("3. VER DATOS DEL ESTUDIANTE")
    print("4. SALIR")
    opcion = input("Selecciona una opcion: ")
    
    if( opcion == "1"):
        print("Escribe los datos del estudiante: (nose podran modificar)")
        matricula = input("Matricula: ")
        nombre = input("Escribe el nombre: ")
        estudiante = EstudianteClass(matricula,nombre)
        
    elif (opcion == "2"):
        while True:
            print("\n\n MENU PARA MODIFICAR \n")
            print("1. ACTUALIZAR TELEFONO")
            print("2. ACTUALIZAR EDAD")
            print("3. ACTUALIZAR PESO")
            print("4. REGRESAR AL MENU ANTERIOR")
            opcion2 = input("Selecciona una opcion: ")
            
            if (opcion2 == "1"):
                telefono = input("Telefono:_")
                estudiante.setTelfono(telefono)
            elif (opcion == "2"):
                edad = input("Edad:_")
                estudiante.setEdad(edad)
            elif (opcion == "3"):
                peso = input("Peso:_")
                estudiante.setPeso(peso)
            elif (opcion == "4"):
                break
            else:
                print("Opcion no valida")
                
    elif (opcion == "3"):
        print("\n\nDATOS DEL ESTUDIANTE:")
        print("Matricula: ", estudiante.getMatricula())
        print("Nombre:", estudiante.getNombre())
        print("Telfono:", estudiante.getTelefono())
        print("Edad:", estudiante.getEdad())
        print("Peso:", estudiante.getPeso())
        
    elif(opcion == "4"):
        print("Adios")
        break
    else:
        print("Opcion no valida")
        
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
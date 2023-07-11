import numpy as np
#https://github.com/Franciscomore/Francisco_Moreno_PGY1121.git
cont = 0
totaldept = np.empty ((10, 4), dtype = object)
for i in range (10):
    for o in range(4):
        cont = cont + 1
        totaldept[i][o] = cont
print(totaldept)

valor = {1: 3800, 2:3000, 3:2800, 4:3500,
         5: 3800, 6:3000, 7:2800, 8:3500,
         9: 3800, 10:3000, 11:2800, 12:3500,
         13: 3800, 14:3000, 15:2800, 16:3500,
         17: 3800, 18:3000, 19:2800, 20:3500,
         21: 3800, 22:3000, 23:2800, 24:3500,
         25: 3800, 26:3000, 27:2800, 28:3500,
         29: 3800, 30:3000, 31:2800, 32:3500,
         33: 3800, 34:3000, 35:2800, 36:3500,
         37: 3800, 38:3000, 39:2800, 40:3500}
vivienda = {}
def compra():
    cont = int(input("ingrese el numero del departamento que comprara "))
    if cont in vivienda:
        print("el departamento que a seleccionado ya que se ha vendido seleccione otro por favor")
    else:
        run = input("por favor ingrese su rut sin puntos,guion y dijito verificador ejemplo: 20495366\n")
        vivienda[cont] = run
        print("el departamento a sido cancelado con exito felicidades")
def depto ():
    disponibilidad = np.copy(totaldept)
    for i in range (10):
        for o in range (4):
            cont = disponibilidad[i][o]
            if int(cont) in vivienda:
                disponibilidad [i][o] = "x"
    print(disponibilidad) 
def lista():
    compra =list(vivienda.items())
    compra.sort()
    for cont,run in compra:
        print(f"depto {cont}:  {run}")
def ganacia():
    ganacia = 0
    for cont in vivienda:
        ganacia += valor[cont]
    print(f"el total obtenidos por la venta de los departamentos es: {ganacia}")

while True:
    print("1 para comprar departamentos")
    print("2 mostar departamentos disponibles")
    print("3 mostar compradores ")
    print("4 mostrar ventas totales")
    print("ingrese cualquier tipo de numero para salir ")
    try:
        
        seleccion = int(input("ingrese la opcion que desea realizar \n"))
       
        if seleccion == 1:
            compra()
        elif seleccion == 2:
            depto()
        elif seleccion == 3:
            lista()
        elif seleccion == 4:
            ganacia()
        else:
            print("adios")
            break
    except (ValueError):
        print("-------------------------------------------------------------------------------")
        print("")
        print("Has cometido un error de validacion por favor ingrese correctamenete los datos")
        print("")
        print("-------------------------------------------------------------------------------")
        
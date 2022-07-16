import os
import readchar
import psutil

# listaDeAplicaciones

listaPre = os.listdir("./")
listaPos = []

for i in listaPre:
    for e in i:
        if e == "-":
            listaPos.append(i)
            break

# variables ---------------------------------------------------------------------------

pos_X = 0
pos_Y = 1

distancia = 6

final = False
pincel = [0, [" "]]

ayuda = [14, 5, "Info", [".leer"]]
plotter = [(ayuda[0]), (ayuda[1] + 3), "Plotter", [".configurar", ".iniciar", ".detener", ".plottInicio"]]
almacenamiento = [(ayuda[0]), (plotter[1] + 3), "Discos", [".ramDisk", ".raid", ".limpiar"]]

programas = [(ayuda[0] + 21), (ayuda[1]), "Programas", listaPos]
energia = [(programas[0]), (programas[1] + 3), "Energia", [".apagar", ".reiniciar"]]
palabra3 = [(energia[0]), (energia[1] + 3), " "]

orden = [[ayuda, plotter, almacenamiento], [programas, energia]]

#                C  N                              C  N            distancia de la flecha;  columna=C numeroDeObjeto=N
flecha = [(orden[0][0][pos_X] - distancia), (orden[0][0][pos_Y]), "==>", 0, 0]
flecha2 = [-1, -1, "///", 0]
flecha3 = [-1, -1, "///", 0]

objetos = []

# menu
titulo2 = [62, 2, "MENU-OPCIONES", False]
titulo1 = [22, 2, "MENU-CENTRAL", True]
menu = [-1, -1, flecha[3], flecha[4]]
minimo = 0
maximo = 4
menus = ["central", "opciones"]
menuAc = "central"
parametros = []

# ventana
ventana = 0
saltarR = False

# clavez
claveC = ""
claveF = ""

# Plantilla1 ------------------------------------------------------------------------

plantilla = """\
##########################################################|---------------------
###                                                    ###|                     
##                                                      ##|                      
#                                                        #|    .                 
#                                                        #|                      
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
#                                                        #|                     
##                                                      ##|                     
###                                                    ###|                     
##########################################################|---------------------\
"""

plantilla = [list(fila) for fila in plantilla.split("\n")]

MAP_ANCHO = len(plantilla[pos_X])
MAP_ALTO = len(plantilla)

# tamaño Canvas

os.system("mode con cols={}".format(MAP_ANCHO + 10))
os.system("mode con lines={}".format(32))


# funciones ----------------------------------------------------------------------

def pincelIn(objeto):
    if objeto in objetos:
        largo = len(objeto[2])
        forma = [list(estructura) for estructura in objeto[2].split("\n")]
        forma = forma[0]
        return [largo, forma]


def cargarDatos():
    if titulo1[3] == True:
        objetos.append(flecha)
    elif titulo2[3] == True:
        objetos.append(flecha2)
        objetos.append(flecha3)
    # elif titulo2[3]== True:
    #     #prenderLaOtraFlecha
    #     return

    objetos.append(ayuda)
    objetos.append(plotter)
    objetos.append(almacenamiento)
    objetos.append(programas)
    objetos.append(energia)
    objetos.append(titulo2)
    objetos.append(titulo1)


def menuEx(poX, poY, columna, fila):
    parametros.clear()
    if [columna, fila] == [0, 0]:
        ayudaM(poX, poY)
    elif [columna, fila] == [0, 1]:
        plotterM(poX, poY)
    elif [columna, fila] == [0, 2]:
        almacenamientoM(poX, poY)
    elif [columna, fila] == [1, 0]:
        programasM(poX, poY)
    elif [columna, fila] == [1, 1]:
        energiaM(poX, poY)


def ayudaM(num1, num2):
    for e in ayuda[3]:
        parametros.append(e)
    for i in (parametros):
        eX = parametros.index(i)
        if eX >= minimo and eX <= maximo:
            num2 = num2 + 2
            objetos.append([num1, num2, i])


def plotterM(num1, num2):
    for e in plotter[3]:
        parametros.append(e)
    for i in (parametros):
        eX = parametros.index(i)
        if eX >= minimo and eX <= maximo:
            num2 = num2 + 2
            objetos.append([num1, num2, i])


def almacenamientoM(num1, num2):
    for e in almacenamiento[3]:
        parametros.append(e)
    for i in (parametros):
        eX = parametros.index(i)
        if eX >= minimo and eX <= maximo:
            num2 = num2 + 2
            objetos.append([num1, num2, i])


def programasM(num1, num2):
    for e in programas[3]:
        parametros.append(e)
    for i in (parametros):
        eX = parametros.index(i)
        if eX >= minimo and eX <= maximo:
            num2 = num2 + 2
            objetos.append([num1, num2, i])


def energiaM(num1, num2):
    for e in energia[3]:
        parametros.append(e)
    for i in (parametros):
        eX = parametros.index(i)
        if eX >= minimo and eX <= maximo:
            num2 = num2 + 2
            objetos.append([num1, num2, i])


def dibuLinea(estilo):
    if estilo == "ancho":
        return (linea * MAP_ANCHO)
    elif estilo == "alto":
        return (linea * MAP_ALTO)


def reiniciarValores():
    minimo = 0
    maximo = 4
    titulo1[3] = True
    titulo2[3] = False
    ventana = 0
    saltarR = True


def guardarParametros(a, b, c, d):
    os.system("asd>datos.txt")
    os.system('echo {} > datos.txt'.format(a))
    os.system('echo {} >> datos.txt'.format(b))
    os.system('echo {} >> datos.txt'.format(c))
    os.system('echo {} >> datos.txt'.format(d))


def cargarParametros(opcion):
    entrada = open('datos.txt')
    salidaSP = entrada.read()
    datos = [letra for letra in salidaSP.split(" \n")]
    return datos[opcion]


def compliladorX():
    plot = 1
    nucleos = cargarParametros(0)
    contrato = cargarParametros(1)
    farmer = cargarParametros(2)
    multipliK = cargarParametros(3)

    complilador = f"-k 32 -n {plot} -r {nucleos} -u 512 -v 256 -t F:\plotts\ -2 R:\plotts\ -d {elegirDisco()}:\plotts\ -c {contrato} -f {farmer} -K {multipliK}"
    os.system("asd>plot.cmd")
    os.system('echo .\chia_plot.exe {} >plot.cmd'.format(str(complilador)))
    os.system('echo exit >>plot.cmd'.format(str(complilador)))


def genOpciones(tex, ancho, margenSup, margen, sangria):
    texP = [list(letra) for letra in tex.split("*")]

    # dibujar----------------------
    print(end=" " * margen)
    for i in range(len(texP)):
        inicio = 0
        print("\n\n", end="")
        linea0 = False
        while inicio < len(texP[i]):
            print(end=" " * margen)
            for d in range(ancho):
                if linea0:
                    if inicio < len(texP[i]):
                        print(texP[i][inicio], end="")
                        inicio = inicio + 1
                else:
                    print(end=" ")
                    if sangria == d:
                        linea0 = True

            if inicio < len(texP[i]):
                print("\n", end="")
    print("\n" * margenSup)


def elegirDisco():
    # generar lista
    letrasU = []
    os.system("fsutil fsinfo drives > discos.txt")
    archivo = open('discos.txt')
    contenido = archivo.read()
    unidades = [list(letra) for letra in contenido.split(" ")]
    for i in range(len(unidades)):
        letrasU.append(unidades[i][0])
    letrasU.pop(0)
    letrasU.pop()

    # seleccionar unidad
    for i in range(len(letrasU) + 1):
        # medir espacio
        excluidas = ["R", "r", "F", "f", "c", "C"]
        fase = str(letrasU[i]) + ":\\"
        discos = psutil.disk_usage(fase)
        espaciolibre = float(discos.free) / 1024 ** 3
        if espaciolibre > 102 and letrasU[i] not in excluidas:
            unidadAct = letrasU[i]
            break
        if i > (len(letrasU)):
            print("\n\n\n       Proceso Finalizado!!")
            input("\n\n\n       Enter para salir...")
            unidadAct = "corte"
    return (unidadAct)


def limpiarDisco():
    if minimo == 2:
        os.system("del F:\plotts\*")
        os.system("del R:\plotts\*")

def plotear(numPlots):

    os.system("mkdir r:\plotts") 
    # prensar un englobamiento externo de plots en paralelo
    for i in range(int(numPlots)):
        os.system("del /F/Q/S F:\plotts\*")
        compliladorX()
        if os.path.exists(elegirDisco() + ":\plotts") == False:
            os.system("mkdir " + elegirDisco() + ":\plotts") 
        os.system("cls")
        if elegirDisco() != "corte":
            os.system("plot.cmd")
    if numPlots == 0:
        while elegirDisco() != "corte":
            os.system("del /F/Q/S F:\plotts\*")
            compliladorX()
            if os.path.exists(elegirDisco() + ":\plotts") == False:
                os.system("mkdir " + elegirDisco() + ":\plotts")
            os.system("cls")
            os.system("plot.cmd")

    os.system("del /F/Q/S F:\plotts\*")

##def propiedadesHard(componente):
##    if componente ==

# Programa /////////////////////////////////////////////////////////////////////////////////////
while final == False:

    os.system("cls")
    menu = [menu[0], menu[1], flecha[3], flecha[4]]
    # menuEx(menu[0], menu[1], menu[2], menu[3])
    # graficar -------------------------------------------------------------------

    linea = "-"
    # Ventana 1 principal ------------------------------------------------------------------------------------
    if ventana == 0:
        print("\n")
        # titulo
        print("   | controlChiaPlotter V 0.4   -----------------------------------------------------|\n")
        # definir
        for coordenadas_y in range(MAP_ALTO):

            print("   | ", end="")
            for coordenadas_X in range(MAP_ANCHO):

                if pincel[0] == 0:

                    # Menu principal
                    menuEx(menu[0], menu[1], menu[2], menu[3])
                    cargarDatos()
                    contador = len(objetos)
                    for i in range(contador):

                        if coordenadas_X == objetos[0][pos_X] and coordenadas_y == objetos[0][pos_Y]:
                            break
                        else:
                            objetos.pop(0)

                    # dibujo
                    if objetos != []:
                        pincel = pincelIn(objetos[0])
                    else:
                        pincel[1][0] = " "
                else:
                    # contador de caracteres restantes antes dar nuevas instrucciones al pincel
                    pincel[0] = pincel[0] - 1

                    # elimina el anterior caracter para dibujar el siguiente
                    if len(pincel[1]) != 1:
                        pincel[1].pop(0)
                    else:
                        pincel[1][0] = " "

                if plantilla[coordenadas_y][coordenadas_X] == "#":
                    pincel[1][0] = "#"
                if plantilla[coordenadas_y][coordenadas_X] == "|":
                    pincel[1][0] = "|"
                if plantilla[coordenadas_y][coordenadas_X] == "-":
                    pincel[1][0] = "-"
                if plantilla[coordenadas_y][coordenadas_X] == ".":
                    flecha3[0] = menu[0] - 4
                    flecha3[1] = menu[1] + 2
                    menu = [coordenadas_X, coordenadas_y, menu[2], menu[3]]
                    flecha2[0] = menu[0] + 13
                    flecha2[1] = menu[1] + 2

                # print(pincel)
                print("{}".format(pincel[1][0]), end="")

            print("|")

        # recuadro inferior
        print("\n"
              "\n     {}"
              "\n"
              "\n       movimiento  |     w     |    cambiar   |   |   ejecutar |   |   cerrar |   | "
              "\n                   | a | s | d |    de menú   | j |   opción   | k |          | x | "
              "\n"
              "\n     {}".format(dibuLinea("ancho"), dibuLinea("ancho")))

    # Ventana 2 info ---------------------------------------------------------------------------------------
    elif ventana == 1:
        print("\n\n\n")
        print("""\
            
         controlChiaPloter V 0.3
         
         programa destinado a controlar y administrar un sistema 
         implicado en la creación de Plotts de la Criptomoneda 
         “Chia”, de momento no tiene más funciones que ejecutar 
         tareas simples, detener procesos, apagar o encender el 
         sistema además de pre configurar parámetros de plotteo.  
                     
                \
                """)
        # recuadro inferior

        print("\n"
              "\n     {}"
              "\n             presione | 'r' para volver | 'x' para salir del programa"
              "\n     {}".format(dibuLinea("ancho"), dibuLinea("ancho")))

    # Ventana 3 configuracion --------------------------------------------------------------------------------
    elif ventana == 2:
        print("\n                   CONFIGURACIÓN ACTUAL DE PLOTTS"
              "\n     --------------------------------------------------------------"
              "\n")
        os.system("type plot.cmd")
        print("\n     --------------------------------------------------------------")

        print("\n"
              "\n"
              "\n     Si no conocés las opciones lo mejor"
              "\n     es dejarlo por default, si estás seguro"
              "\n     que querés seguir escribi 'SI' (sin"
              "\n     las comillas) y presioná enter, sino"
              "\n     simplemente presioná enter"
              "\n     ")
        seguir = (str(input("     continuar?:")))

        if seguir == "SI" or seguir == "si":

            # cantidad de nucleos
            os.system("cls")
            print("\n\n")
            genOpciones("Cantidad de hilos de procesamiento, si lo dejás en blanco por defecto serán 4", 40, 4, 5, 3)
            r = str(input("    número de hilos: "))
            if r == "":
                r = "4"

            # Dir Temporal 1
            t = "F:\plotts\ "
            os.system("mkdir {}".format(str(t)))

            # Dir Temporal 2 (RAM)
            raid = "R:\plotts\ "
            os.system("mkdir {}".format(str(raid)))

            # Poolkey
            os.system("cls")
            print("\n\n")
            c = str(input("\n"
                          "\n     dirección pública de 62 caracteres: "))

            # FarmerKey
            os.system("cls")
            print("\n\n")
            f = str(input("\n"
                          "\n     llave pública de 48 bytes: "))

            # Multiplicador de nucleos
            os.system("cls")
            print("\n\n")
            genOpciones("ultiplicador de hilos de procesamiento Si lo dejás en blanco por defecto será 1", 40, 4, 5, 3)
            K = str(input("\n"
                          "\n     Multiplicador: "))

            # ---- Generar Archivo ----
            forma = ["salir", "SALIR", "exportar", "EXPORTAR"]
            enviar = ""
            while enviar not in forma:
                # Archivo Final
                os.system("cls")
                print("\n\n")
                genOpciones(
                    "si estás seguro de que esta es la config correcta escribí 'exportar'.*si querés salir sin "
                    "guardar 'salir'.",
                    40, 4, 5, 3)
                enviar = str(input("\n               acción?: "))
            if enviar == "salir" or enviar == "SALIR":
                minimo = 0
                maximo = 4
                titulo1[3] = True
                titulo2[3] = False
                ventana = 0
                saltarR = True
            elif enviar == "exportar" or enviar == "EXPORTAR":
                guardarParametros(r, c, f, K)
                minimo = 0
                maximo = 4
                titulo1[3] = True
                titulo2[3] = False
                ventana = 0
                saltarR = True

        else:
            minimo = 0
            maximo = 4
            titulo1[3] = True
            titulo2[3] = False
            ventana = 0
            saltarR = True

        # controlDebug

    if False:
        print("\n"
              "    altura X {} | Y {}".format(MAP_ANCHO, MAP_ALTO))

        print("\n    posicion - | {} | {} |    Menu - | {} | {} |-| {} | {} |"
              "\n"
              "\n    parametros - | {} |   min {} max {}"
              "".format(flecha[3], flecha[4], menu[0], menu[1], menu[2], menu[3], parametros, minimo, maximo))

    # Controles---------------------------------------------------------------------------------------------------

    if saltarR == False:
        opcion = readchar.readchar().decode()
    else:
        saltarR = False

    # VENTANA 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if ventana == 0:
        # cambiar de menu
        if opcion == "j":
            if titulo1[3] == True:
                titulo2[3] = True
                titulo1[3] = False
            else:
                minimo = 0
                maximo = 4
                titulo1[3] = True
                titulo2[3] = False

        # MENU-CENTRAL/////////////////////////////////////////////////////////////////////////////////////////
        if titulo1[3] == True:

            if opcion == "d":

                if flecha[3] < (len(orden) - 1):
                    if flecha[4] > (len(orden[(flecha[3] + 1)]) - 1):
                        flecha[4] = (len(orden[flecha[3] + 1]) - 1)
                        flecha[1] = orden[flecha[3]][flecha[4]][1]
                    flecha[3] = flecha[3] + 1
                    flecha[0] = orden[flecha[3]][0][0] - distancia

            elif opcion == "a":
                if flecha[3] > 0:
                    flecha[3] = flecha[3] - 1
                    flecha[0] = orden[flecha[3]][0][0] - distancia

            elif opcion == "s":
                if flecha[4] < (len(orden[flecha[3]]) - 1):
                    flecha[4] = flecha[4] + 1
                    flecha[1] = orden[flecha[3]][flecha[4]][1]

            elif opcion == "w":
                if flecha[4] > 0:
                    flecha[4] = flecha[4] - 1
                    flecha[1] = orden[flecha[3]][flecha[4]][1]

        # MENU2-OPCIONES//////////////////////////////////////////////////////////////////////////////////////////
        if titulo2[3] == True:

            if opcion == "k":
                # Info
                if [menu[2], menu[3]] == [0, 0]:
                    # leer
                    if minimo == 0:
                        ventana = 1
                # Plotter
                elif [menu[2], menu[3]] == [0, 1]:
                    # configuracion
                    if minimo == 0:
                        ventana = 2
                    # iniciar
                    elif minimo == 1:
                        genOpciones("Indica la cantidad de plots que quieras generar.*Si querés cancelar escribi 'no' "
                                    "(en minusculas, si querés plotear hasta que no exista mas lugar indica '0')", 30, 5, 4, 3)
                        nPlots = int(input("\n\n\n Cantidad: "))
                        plotear(nPlots)
                    # Detener
                    elif minimo == 2:
                        os.system("taskkill /f /im chia_plot.exe")
                    # # plottInicio
                    elif minimo == 3:
                        os.system("cls")
                        desiciones = ["si", "no", "SI", "NO"]
                        desicion = ""
                        while desicion not in desiciones:
                            desicion = str(input("\n\n\n\n\n\n   iniciar plotteo con windows? [si] | [no] :"))

                        if desicion == "si" or desicion == "SI":
                            os.system("echo plot > arranque.cmd")
                        elif desicion == "no" or desicion == "NO":
                            os.system("asd > arranque.cmd")

                # DISCOS
                elif [menu[2], menu[3]] == [0, 2]:
                    # ramdisk
                    if minimo == 0:
                        os.system("start -asdd.docx")
                    # raid
                    if minimo == 1:
                        os.system("control /name Microsoft.StorageSpaces")
                    # limpiar
                    if minimo == 2:
                        os.system("del F:\plotts\*")
                        os.system("del R:\plotts\*")
                # PROGRAMAS
                elif [menu[2], menu[3]] == [1, 0]:
                    # programas
                    os.system("start {}".format(listaPos[minimo]))
                # Energia
                elif [menu[2], menu[3]] == [1, 1]:
                    # Apagar
                    if minimo == 0:
                        os.system("shutdown /s /t 5")
                    # Reiniciar
                    if minimo == 1:
                        os.system("shutdown /s /t 5")

            if opcion == "w":
                if minimo > (0):
                    minimo = minimo - 1
                    maximo = maximo - 1

            if opcion == "s":
                if maximo < (len(parametros) + 3):
                    minimo = minimo + 1
                    maximo = maximo + 1

    # VENTANA 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # VENTANA 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if ventana == 1 or ventana == 2:
        if opcion == "r":
            minimo = 0
            maximo = 4
            titulo1[3] = True
            titulo2[3] = False
            ventana = 0

        #
        # elif opcion == "s":
        #     if flecha[4] < (len(orden[flecha[3]]) - 1):
        #         flecha[4] = flecha[4] + 1
        #         flecha[1] = orden[flecha[3]][flecha[4]][1]

    # cerrar
    if opcion == "x":
        os.system("cls")
        final = True
        print("\n\n\n\n"
              "\n\n                      si querés volver a prender el programa "
              "\n                               solo tenés que escribir"
              "\n"
              "\n                                    'plotteradmin'              "
              "\n"
              "\n                             en cualquier ventana de CMD")
        input("\n\n\n    enter para salir...")

    os.system("cls")

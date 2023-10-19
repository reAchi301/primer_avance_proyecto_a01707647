"""
Autor: Ricardo Calzada Hernández
Matricula: A01707647
Última fecha de actuaización: 17/10/23

EmeK:Calculadora de valores de mercado futbolístico
El programa cuestiona al usuario acerca de  un jugador en específico
para que al final del programa proporcione un rango de
valor de mercado además de un resumen del jugador analizado.
"""

#biblioteca
import math

"""
================== funciones de sumas y restas ==========================
Estas funciones sirven para añadir o disminuir ciertos valores a
la variable (resultado)
Reciben: Variable resultado
Devuelven: Variable resultado con valor añadido
"""
def suma_maxima(resultado):
    res_5 = resultado + 5
    return res_5
def suma_destacable(resultado):
    res_4 = resultado + 4
    return res_4
def suma_intermedia(resultado):
    res_3 = resultado + 3
    return res_3
def suma_pequeña(resultado):
    res_2 = resultado + 2
    return res_2
def suma_unitaria(resultado):
    res_1 = resultado + 1
    return res_1
def suma_nula(resultado):
    res_cero = resultado + 0
    return res_cero
def resta_maxima(resultado):
    res_restamax = resultado - 5
    return res_restamax
def resta_mediana (resultado):
    res_restamed = resultado - 2
    return res_restamed
"""
================== funciones de finalización ============================
"""
    
def contador (lista):
    """
    Contiene un contador que inicia en 0, se usa un ciclo for
    para que recorra los componentes de la lista y por cada
    elemento de la lista que recorra se le sume "1" al contador.
    Básicamente cuenta el número de elementos que contiene la lista.
    Recibe: Lista
    Devuelve: el contador
    """
    cont = 0
    for i in lista:
        cont = cont + 1
    return cont
    

def promedio (lista):
    """
    La variable "divison" se encarga de dividir el elemento 0 / el
    elemento 1 de la lista, con el objetivo de dar un promedio
    que servirá para determinar el precio del jugador. 
    Recibe: lista
    Devuelve: la variable division
    """
    division = lista[0] / lista[1]
    return division
          
#Lista que va a almacenar todos los jugadores calculados por el usuario
jugadores_calculados = []


"""
================== PROGRAMA PRINCIPAL ============================
"""
    
    
"""
Se mete en un ciclo while todo el programa para poder hacer la repetición del
programa al final del mismo
"""

while True:
    print("Bienvenido a EmeK\nTu calculadora de valores"
          " de mercado futbolístico de"
          " confianza\nInstrucciones generales:\nResponde"
          " todo tal como se te pide, para"
          " respuestas tipo cadena escribir todo en minúsculas")
    
    ligas = ["Premier League","La Liga", "Bundesliga", "Serie A"
            , "Ligue 1"]
    
    nacion_ligas = [" (Inglaterra)"," (España)", " (Alemania)", " (Italia)"
            , " (Francia)"]
    
    resumen_ligas = [ligas[0]+nacion_ligas[0], ligas[1]+nacion_ligas[1],
                   ligas[2]+nacion_ligas[2], ligas[3]+nacion_ligas[3],
                   ligas[4]+nacion_ligas[4]]
    
    print("Las 5 grandes ligas son:",resumen_ligas)
    nombre_jugador = str(input("Introduce el nombre de un jugador de las "
                              "5 grandes ligas de Europa:\n"))
  
    """
    lista a la que se le van a ir añadiendo valores para posterior-
    mente usarlos en un contador que definirá el promedio
    """
    task_count = []
    
    #variable resultado que almacenará todas las sumas
    resultado = 0
    
    #Variable de entrada para guardar la liga del jugador
    liga_jugador = (str(input("Introduce el nombre de la liga en "
                        " la que juega el jugador:\n")))
    

    if liga_jugador == "premier league":
        resultado = suma_maxima(resultado)
    elif liga_jugador == "la liga":
        resultado = suma_destacable(resultado)
    elif liga_jugador == "bundesliga":
        resultado = suma_intermedia(resultado)
    elif liga_jugador == "serie a":
        resultado = suma_pequeña(resultado)
    elif liga_jugador == "ligue 1":
        resultado = suma_unitaria(resultado)
    """   
    Estos task_count se irán añadiendo al final de cada sección, ya que
    añadirán valores a la lista que será usada en la función
    contador(lista)
    """
    task_count.append(1)
    
    #Variable de entrada para guardar la edad del jugador
    edad_jugador = (int(input("Introduzca la edad del jugador:\n")))

    if  edad_jugador >= 17 and edad_jugador <= 23 :
        resultado = suma_maxima(resultado)
    elif edad_jugador  >= 24 and edad_jugador <= 27:
        resultado = suma_intermedia(resultado)
    elif edad_jugador  >= 28 and edad_jugador <= 34:
        resultado = suma_pequeña(resultado)
    elif edad_jugador  >= 35 and edad_jugador <= 41:
        resultado = suma_unitaria(resultado)
    elif edad_jugador >= 42:
        resultado = resta_maxima(resultado)
        
    task_count.append(2)
    
    
    #Se meten las nacionalidades dentro de listas 
    naci_top5 = ["francia", "brasil", "inglaterra","argentina",
           "bélgica"]
    naci_top10 = ["croacia", "paises bajos", "italia", "portugal",
            "españa"]
    naci_top15 = ["estados unidos","méxico", "suiza", "marruecos"
            ,"alemania"]
    
    print("Escribe 1 para nacionalidades TOP 5:\n",naci_top5)
    print("Escribe 2 para nacionalidades TOP 10:\n",naci_top10)
    print("Escribe 3 para nacionalidades TOP 15:\n",naci_top15)


    #Variable de entrada para guardar la nacion del jugador
    nacion_jugador=(int(input("Introduce el número de la nacionalidad"
                                " del jugador:\n")))
    task_count.append(3)
    
    if nacion_jugador == 1:
        resultado = suma_maxima(resultado)
    elif nacion_jugador == 2:
        resultado = suma_intermedia(resultado)
    elif nacion_jugador == 3:
        resultado = suma_unitaria(resultado)
    else:
        resultado = suma_nula(resultado)
        
    #2 variables de entrada que serán sumadas para poder crear un total
    goles_jugador = (int(input("Introduce la cantidad de goles de tu jugador "
                               "en su última temporada jugada:\n")))
    asistencias_jugador = (int(input("Introduce la cantidad de asistencias "
                                    "de tu jugador en su última "
                                     "temporada jugada:\n")))
    
    estadisticas_totales = goles_jugador + asistencias_jugador
    
    if  estadisticas_totales >= 30:
        resultado = suma_maxima(resultado)
    elif estadisticas_totales >= 23 and estadisticas_totales < 30:
        resultado = suma_intermedia(resultado)
    elif estadisticas_totales >= 18 and estadisticas_totales < 23:
        resultado = suma_pequeña(resultado)
    elif estadisticas_totales >= 10 and estadisticas_totales < 18:
        resultado = suma_unitaria(resultado)
    elif estadisticas_totales >= 5 and estadisticas_totales < 10:
        resultado = suma_nula(resultado)
        
    task_count.append(4)
   
    #
    seleccion_jugador = (bool(input("¿El jugador ha sido llamado a su "
                                  "seleccion nacional? (True or False)\n")))
    
    if seleccion_jugador == True:
        resultado=suma_intermedia(resultado)
        task_count.append(5)
        seleccion_apariciones = (bool(input("¿Las veces que fue convocado "
                                            "se desempeñó destacadamente? "
                                            "(True or False)\n")))
        if seleccion_apariciones == True:
            resultado = suma_pequeña(resultado)
            task_count.append(6)
        elif seleccion_apariciones == False:
            resultado = resta_mediana(resultado)
            task_count.append(7)
    elif seleccion_jugador == False:
        resultado = resta_mediana(resultado)
        task_count.append(8)


    #Variable de entrada para guardar la posición del jugador
    posicion_jugador = (str(input("Introduce la posición del jugador: "
                                  "portero, defensor, mediocampista, "
                                  "delantero :\n")))

    if posicion_jugador == "delantero":
        resultado = suma_maxima(resultado)
    elif posicion_jugador == "mediocampista":
        resultado = suma_destacable(resultado)
    elif posicion_jugador == "defensor":
        resultado = suma_intermedia(resultado)
    elif posicion_jugador == "portero":
        resultado = suma_unitaria(resultado)
    
    task_count.append(9)
    
    precio_jugador = (int(input("Introduce la última cantidad "
                        "de millones de euros que se cobró por "
                                "el jugador:\n")))
    if  precio_jugador >= 100:
        resultado = suma_maxima(resultado)
    elif precio_jugador >= 80 and precio_jugador < 100:
        resultado = suma_destacable(resultado)
    elif precio_jugador >= 60 and precio_jugador < 80:
        resultado = suma_intermedia(resultado)
    elif precio_jugador >= 30 and precio_jugador < 60:
        resultado = suma_pequeña(resultado)
    elif precio_jugador >= 15 and precio_jugador < 30:
        resultado = suma_unitaria(resultado)
    
    task_count.append(10)
    
    """
    Se guardan las dos variables importantes dentro de una lista para poder
    hacer uso de la función que nos va a dar el promedio que delimitrá el
    precio de nuestro jugador
    """
    #Valor absoluto de la variable resultado
    math.fabs(resultado)
    
    variables_importantes = [resultado, contador(task_count)]


    PROMEDIO_IMP = promedio(variables_importantes)
    
    """
    Mediante la manipulación de carácteres se crea el resultado final
    del proyecto en base a los promedios que nuestras funciones creen
    """
    valor_de_mercado = ("El precio del jugador ronda entre los ")
    
    if PROMEDIO_IMP >= 4.00:
        valor_de_mercado = valor_de_mercado + "200 MDE y 120 MDE"
    elif PROMEDIO_IMP >= 3.50 and PROMEDIO_IMP < 4.00:
        valor_de_mercado = valor_de_mercado + "120 MDE y 90 MDE"
    elif PROMEDIO_IMP >= 2.00 and PROMEDIO_IMP < 3.50:
        valor_de_mercado = valor_de_mercado + "90 MDE y 75 MDE"
    elif PROMEDIO_IMP >= 2.50 and PROMEDIO_IMP < 2.00:
        valor_de_mercado = valor_de_mercado + "75 MDE y 50 MDE"
    elif PROMEDIO_IMP >= 2.00 and PROMEDIO_IMP < 2.50:
        valor_de_mercado = valor_de_mercado + "50 MDE y 25 MDE"
    elif PROMEDIO_IMP >= 1.50 and PROMEDIO_IMP < 2.00:
        valor_de_mercado = valor_de_mercado + "25 MDE y 10 MDE"
    elif PROMEDIO_IMP >= 1.00 and PROMEDIO_IMP < 1.50:
        valor_de_mercado = valor_de_mercado + "10 MDE y 5 MDE"
    else:
        valor_de_mercado = valor_de_mercado + "5 MDE y 1 MDE"
        
    """
    Se agrega  y se imprime un diccionario para poder mostrar
    un resumen del jugador que ha sido analizado
    
    """
    dict={"Nombre:":nombre_jugador,"Liga:":liga_jugador,"Edad:":edad_jugador,
          "Nación:":nacion_jugador,"Posición:":posicion_jugador,
          "Evaluación:":valor_de_mercado}
    
    print("El resumen de el jugador analizado es el siguiente\n", dict)
    
    #Se almacena la info del jugador dentro de la lista jugadores_calculados 
    jugadores_calculados.append(dict)
    
    #se pregunta al usuario si quiere culminar con el programa
    repeticion = input("¿Deseas calcular el valor de mercado de otro "
                       "jugador? (si/no): ")
    
    """
    En caso de que el usuario decida poner (si) el programa se corre
    una vez más. Pero si el usuario responde con una respuesta diferente a
    (si) se imprime un mensaje de despedida, todos los jugadores que el usuario
    calculó y cierra el programa
    """
    if repeticion.lower() != "si":
        print("Resumen:", jugadores_calculados)
        print("Gracias por usar EmeK, ¡vuelve pronto!")
        break
















    
     
   


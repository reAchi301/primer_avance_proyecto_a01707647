print("Bienvenido a EmeK\nTu calculadora de valores de mercado fubtolístico de"
      "confianza\nInstrucciones generales:\nResponde todo tal como se te pide, para"
      "respuestas tipo cadena escribir todo en minúsculas")

#Variable de entrada para guardar el nombre del jugador
nombre_jugador=(str(input("Introduce el nombre de un jugador de las 5 grandes"
     "ligas de Europa:\n(Premier League, La Liga,"
     "Bundesliga, Serie A, Ligue 1)\n")))

resultado=0
#Funciones que van a cumplir con el objetivo de sumar nuevos valores a la variable
#resultado y así empezar a determinar el rango en el que se encuentra el jugador
def suma_maxima(resultado):
    res_5=resultado+5
    return res_5
def suma_destacable(resultado):
    res_4=resultado+4
    return res_4
def suma_intermedia(resultado):
    res_3=resultado+3
    return res_3
def suma_pequeña(resultado):
    res_2=resultado+2
    return res_2
def suma_unitaria(resultado):
    res_1=resultado+1
    return res_1
def suma_nula(resultado):
    res_cero=resultado+0
    return res_cero

#Variable de entrada para guardar la liga del jugador
liga_jugador=(str(input("Introduce el nombre de la liga en la que juega el"
     "jugador(Premier League,La Liga, Bundesliga, Serie A, Ligue 1)\n")))

if liga_jugador == "premier league":
    resultado = suma_maxima(resultado)
elif liga_jugador == "la liga":
    resultado = suma_destacable(resultado)
elif liga_jugador == "bundesliga":
    resultado= suma_intermedia(resultado)
elif liga_jugador == "serie a":
    resultado= suma_pequeña(resultado)
elif liga_jugador == "ligue 1":
    resultado= suma_unitaria(resultado)
#Variable de entrada para guardar la edad del jugador
edad_jugador=(int(input("Introduzca la edad del jugador\n")))

if  edad_jugador >=17 and edad_jugador <=23 :
    resultado = suma_maxima(resultado)
elif edad_jugador  >=24 and edad_jugador <=27:
    resultado= suma_intermedia(resultado)
elif edad_jugador  >=28 and edad_jugador <=34:
    resultado= suma_pequeña(resultado)
elif edad_jugador  >=35 and edad_jugador <=41:
    resultado=suma_unitaria(resultado)
elif edad_jugador >=42:
    resultado=suma_nula(resultado)

print("Escribe 1 para nacionalidades TOP 5:francia","brasil","inglaterra",
      "argentina","bélgica\n")
print("Escribe 2 para nacionalidades TOP10: croacia","paises bajos",
      "italia","portugal","españa\n")
print("Escribe 3 para nacionalidades TOP 15: estados unidos","méxico",
      "suiza","marruecos","alemania\n")

#Variable de entrada para guardar la nacion del jugador
nacion_jugador=(int(input("Introduce el numero de la nacionalidad del jugador\n")))
if nacion_jugador==1:
    resultado=suma_maxima(resultado)
elif nacion_jugador==2:
    resultado=suma_intermedia(resultado)
elif nacion_jugador==3:
    resultado=suma_unitaria(resultado)
else:
    resultado=suma_nula(resultado)

#Variable de entrada para guardar la posición del jugador
posicion_jugador=(str(input("Introduce la posición del jugador: portero,"
     "defensor, mediocampista, delantero\n")))

if posicion_jugador == "delantero":
    resultado=suma_maxima(resultado)
elif posicion_jugador == "mediocampista":
    resultado=suma_destacable(resultado)
elif posicion_jugador == "defensor":
    resultado=suma_intermedia(resultado)
elif posicion_jugador == "portero":
    resultado=suma_unitaria(resultado)
"""
Termino el código con la función que me va a ayudar a sacar el rango para poder
clasificar en que precio se van a ir acomodando el diferente tipo de jugadores,
esto va a estar delimitado por condicionales que van a determinar si el resultado
de la función "rango" es correspondiente a ciertos precios.
"""

def rango (n1):
    res_final=n1/4
    return res_final
var_final= rango(resultado)
print(var_final)  

"""
Después de la linea de código de "posición_jugador" se tiene planeado hacer
preguntas con variable de tipo boolean, las cuales aun no han sido vistas en
clase y por consecuencia no son requerimiento en esta entrega de avance
del proyecto. En pseudocódigo sería algo mas o menos así:

E0=
lesiones_jugador= (bool(input(El jugador es propenso a lesiones?)))
si lesiones_jugador = True:
  resultado=resultado-5
else
  resultado=resultado+5
EF= resultado con un valor mas añadido

E0=
seleccion_jug=(bool(input(El jugador ha sido llamado a su seleccion nacional?)))
si seleccion_jug=True
   resultado=resultado+2
   seleccion_apariciones=(bool(input(Las veces que fue convocado se desempeñó
   destacadamente?)))
      si seleccion_apariciones=True:
         resultado=resultado+3
      else
         resultado=resultado-3
else
   resultado=-2
EF= resultado con valor actualizado
"""





    
     
   


   


    
     
   


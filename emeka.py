#Darle una calida bienvenida al usuario

print("Bienvenido a EmeK\nTu calculadora de valores de mercado fubtolístico de confianza\nInstrucciones generales:\nResponde todo tal como se te pide, para respuestas tipo cadena escribir"
      " todo en minúsculas")
#definir una variable de cadena con entrada para reconocer el nombre del jugador
nombre_jugador=(str(input("Introduce el nombre de un jugador de las 5 grandes ligas de Europa:\n(Premier League,La Liga, Bundesliga, Serie A, Ligue 1)\n")))
#definir una variable entera para poder ir acumulando una suma de resultados para que al final el programa pueda desplegar un resultado en base a la suma
resultado=0
#definir variable de entrada, valor de cadena para guardar la liga del jugador, en base a que liga es la suma que se le va a dar con condicionales se les dara un valor distinto a la varia
#ble resultado
liga_jugador=(str(input("Introduce el nombre de la liga en la que juega el jugador(Premier League,La Liga, Bundesliga, Serie A, Ligue 1)\n")))

if liga_jugador == "premier league":
    resultado=resultado+5
elif liga_jugador == "la liga":
    resultado=resultado+4
elif liga_jugador == "bundesliga":
    resultado=resultado+3
elif liga_jugador == "serie a":
    resultado=resultado+2
elif liga_jugador == "ligue 1":
    resultado=resultado+1
#definir otra variable de entrada, esta vez entera para guardar la edad del jugador, posteriormente mediante el uso de condicionales en base a los rangos de edad del jugador cambiar nueva
#mente el valor de la variable resultado
edad_jugador=(int(input("Introduzca la edad del jugador\n")))

if  edad_jugador >=17 and edad_jugador <=23 :
    resultado=resultado+5
elif edad_jugador  >=24 and edad_jugador <=27:
    resultado=resultado+3
elif edad_jugador  >=28 and edad_jugador <=34:
    resultado=resultado+2
elif edad_jugador  >=35 and edad_jugador <=41:
    resultado=resultado+1
elif edad_jugador >=42:
    resultado=resultado+0

#Darle nuevas instrucciones al usuario
#variable de entrada de tipo entero para poder denominar la nacionalidad del jugador y añadirle un nuevo valor a la variable resultado
print("Escribe 1 para nacionalidades TOP 5:francia","brasil","inglaterra","argentina","bélgica\n")
print("Escribe 2 para nacionalidades TOP10: croacia","paises bajos","italia","portugal","españa\n")
print("Escribe 3 para nacionalidades TOP 15: estados unidos","méxico","suiza","marruecos","alemania\n")

nacion_jugador=(int(input("Introduce el numero de la nacionalidad del jugador\n")))
if nacion_jugador==1:
    resultado=resultado+5
elif nacion_jugador==2:
    resultado=resultado+3
elif nacion_jugador==3:
    resultado=resultado+1
else:
    resultado=resultado+0

#definir variable de entrada  de cadena para guardar la posicion del jugador, en base a que posición sea va a sere la suma que se le va a dar mediante
#condicionales se les dara un valor distinto a la variable resultado
posicion_jugador=(str(input("Introduce la posición del jugador: portero, defensor, mediocampista, delantero)\n")))

if posicion_jugador == "delantero":
    resultado=resultado+6
elif posicion_jugador == "mediocampista":
    resultado=resultado+5
elif posicion_jugador == "defensor":
    resultado=resultado+4
elif posicion_jugador == "portero":
    resultado=resultado+1
#funcion para dar el resultado final de todas las sumas, el cual se va a determinar por (resultado de sumas/numero de sumas) en este caso son 4 sumas, por lo que se dividirá entre 4
def rango (n1):
    res_final=n1/4
    return res_final
var_final= rango(resultado)
print(var_final)    

"""
Termino el código con la función que me va a ayudar a sacar el rango para poder clasificar en que precio se van a ir acomodando el diferente tipo de jugadores, esto va a estar delimitado
por condicionales que van a determinar si el resultado de la función "rango" es correspondiente a ciertos precios.
"""
"""
Después de la linea de código de "posición_jugador" se tiene planeado hacer preguntas con variable de tipo boolean, las cuales aun no han sido vistas en clase y por consecuencia no son requerimiento en esta entrega de avance
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
   seleccion_apariciones=(bool(input(Las veces que fue convocado se desempeñó destacadamente?)))
      si seleccion_apariciones=True:
         resultado=resultado+3
      else
         resultado=resultado-3
else
   resultado=-2
EF= resultado con valor actualizado
"""
   


    
     
   


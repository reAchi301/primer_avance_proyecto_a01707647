# primer_avance_proyecto_a01707647
CALCULADORA DE VALORES DE MERCADO DE UN JUGADOR DE FUTBOL

 Hoy en día se sabe que el fútbol no es solo un deporte, sino que es visto mayormente como un negocio. Como resultado los jugadores no solo son tomados en cuenta  
 como profesionistas sino como un producto de donde los clubes sacan provecho. Por lo mismo, cada jugador tiene un valor de mercado el cuál se 
 mide bajo varios párametros. Entre los cuales se encuentran 

Transferencias anteriores, edad del jugador y su potencial futuro, la posición, rendimiento actual en clubes y selecciones, la situación institucional del club al que pertenece, estado físico y regularidad de cara a lesiones, interés de otros clubes, la trayectoria y experiencia profesional, prestigio internacional, sueldo y jerarquía dentro del club o potencial como marca publicitaria. Gómez, E. (2019)

Es importante tener en cuenta el no confundir el "valor de mercado" con el "precio final" del futbolista, ya que el valor de mercado es más como un estimado a 
lo que diferentes clubes estarían pagando por él por parejo y el "precio final" es la cifra máxima que un club ofreció/puede ofrecer por dicho jugador. También aclarar que el mercado cambia continuamente dependiendo de los eventos que ocurren del mismo, por ejemplo, si un club compra por cierta cantidad a un jugador los demás clubes empezarán a tomar como referencia esa transacción en base a sus propios jugadores, entre otras situaciones.

Dicho lo anterior, lo que se buscará con este proyecto será desarrollar un programa en el que con el hecho de introducir ciertos datos relacionados a algunos de los párametros anteriormente mencionados (usando variables de tipo string, boolean e integer) y que mediante el uso de condicionales pueda validar en base a los resultados que el usuario arroje de que clase de jugador se está hablando, para que de la misma manera vaya acumulando los resultados dados y así el programa dé como resultado el valor de mercado del jugador que el usuario desea saber.

Referencias API de Phyton

Librería: Math

Utilizada dentro de este programa para poder calcular el valor absoluto de la variable resultado, que nos permite dar conclusión al objetivo del programa, se utilizó porque había unas situaciones en las que la variable tomaba un valor negativo que podía generar confusión dentro del programa.

Este módulo proporciona acceso a las funciones matemáticas definidas en el estándar de C.

Estas funciones no pueden ser usadas con números complejos; usa las funciones con el mismo nombre del módulo cmath si requieres soporte para números complejos. La distinción entre las funciones que admiten números complejos y las que no se hace debido a que la mayoría de los usuarios no quieren aprender tantas matemáticas como se requiere para comprender los números complejos. Recibir una excepción en lugar de un resultado complejo permite la detección temprana del número complejo inesperado utilizado como parámetro, de modo que el programador pueda determinar cómo y porqué se generó en primer lugar.

Este módulo proporciona las funciones descritas a continuación. Excepto cuando se indique lo contrario explícitamente, todos los valores retornados son flotantes. (Phyton, 2023).

Fuentes:
- Gómez, E. (2019, 27 de agosto). Así calcula Transfermarkt el valor de los jugadores de fútbol. Diario AS. https://as.com/futbol/2019/08/27/mas_futbol/1566863263_499442.html
- math — Funciones matemáticas — documentación de Python - 3.12.0. (n.d.). Python Docs. Retrieved October 18, 2023, from https://docs.python.org/es/3/library/math.html

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Subcompetencia original:
Integración del API

Cambio Realizado:
Se incluyó la biblioteca Math para calcular el valor absoluto de la variable resultado ya que en algunos casos podía salir negativa.

Lineas del código donde se puede encontrar: 13 y 262

Subcompetencia original:

Formato Pep 8

Cambio Realizado:

Se corrigió formato en su totalidad, desde los comentarios dentro de las funciones, hasta la misma presentación del programa

Lineas del código donde se puede encontrar: de la 1 a 318

Subcompetencia original:

Funciones

Cambio Realizado:

Ejemplo : 

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

Se sacaron las funciones del ciclo while y se corrigió su formato.

Lineas del código donde se puede encontrar: de la 22 a 74

Subcompetencia original:

Estandáres

Cambio Realizado:

Eliminé los archivos extra en el repositorio, corregí el formato entero de mi código con los lineamientos del PEP8

Lineas del código donde se puede encontrar: de la 1 a la 295

Subcompetencia original:

Tecnologías

Cambio Realizado:

Se buscó como objetivo estar dentro de los lineamientos requeridos

Lineas del código donde se puede encontrar: de la 1 a la 295

Avances

Avance 1: Plantea una situación problema que le permite aplicar y demostrar sus conocimientos de programación (avance 1) 17/08/2023

Avance 2: Usa operadores aritméticos de manera eficaz (avance 2) 24/08/2023

Avance 3: Incorpora a tu proyecto libre uso de funciones. 31/08/2023

Avance 4: Aplica estructuras condicionales para resolver un problema (avance 4) 07/09/2023
Ya se incluían condicionales desde la primer entrega, pero se aññadieron más ahora de variable booleana.

Avance 5: Se aplica el uso de ciclos while 21/09/2023

Avance 6: Se aplican listas 28/09/2023

Avance 7: Se aplican listas anidadas 05/10/23

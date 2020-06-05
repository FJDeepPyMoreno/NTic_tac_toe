# Creación de objetos TableroNR de tamaño arbitratio cuadrado.
# Se podrán colocar fichas de dos tipos en el tablero: fichaa, fichab


import numpy as np
from random import choice
from os import strerror

###################################################################################
# TableroNR class:
#
#  -- Constructor:
#
#      'fichaa' : primer tipo de ficha, por ejemplo: 'X', 'O', o lo que sea
#      'fichab' : segundo tipo de ficha. Símbolo que queramos para dicha ficha.
#      'tamanio' : tamaño de lado del tablero. El número de casillas será tamanio ** 2
#
# -- Atributos:
#
#      'confi': lista bidimensional que almacena el estado actual del tablero. Este
#               atributo se inicializa a espacios vacíos cuando se crea un objeto.
#
#      'tablero_restante': es una lista unidimensional que almacena las casillas que aun
#                           están vacías. Resulta fundamental para ahorrar tiempo de
#                           computación y así evitar que se seleccionen casillas ya
#                           ocupadas. Escogeremos casillas del 'tablero_restante' para
#                           ir metiendo las fichas.
#
#       'message_ganar': nos dice cuál ha sido el motivo del fin del juego:
#                        'línea horizontal', 'línea vertical', o 'línea diagonal'.
#
#       'fin_de_juego': flag que cuando se pone a True, finaliza el juego. Esto ocurre
#                       cuando algún jugador ha ganado la partida o bien cuando se acaban
#                       las fichas.

class TableroNR:
    def __init__(self, fichaa, fichab, tamanio):
        self.confi =[['' for x in range(tamanio)] for y in range(tamanio)]
        self.tamanio = tamanio
        self.fichaa = fichaa   # Tipos de fichas que usaremos
        self.fichab = fichab
        self.tablero_restante=[i for i in range(1,tamanio ** 2 + 1)]
        self.message_ganar ="N"
        # tablero_restante está formado por una lista unidimensional que hace referencia
        # a las casillas del tablero que aún no tienen ficha.
        # En cada movimiento, se eliminará el elemento de la lista correspondiente
        # de modo que a medida que avance el juego quedarán menos casillas libres.

        self.fin_de_juego = False

    def movimiento(self, ficha, destiRow, destiColumn):
        # destiRow y destiColumn se pasarán en un rango entre 1 y el tamaño del lado
        # del tablero.
        # 'ficha' será el símbolo correspondiente al tipo de ficha que metamos en el
        # tablero.

        # Primero miramos si la casilla elegida al azar no está ocupada:

        if(self.confi[destiRow-1][destiColumn-1] != ''):
            # Para minimizar tiempo de computación, solo de podrán elegir las casillas
            # disponibles.
            elem = choice(self.tablero_restante)
            # Hay que transformar el elemento del array unidimensional en su valor de
            # fila y columna:
            if elem % self.tamanio == 0:
                 columna = self.tamanio
                 fila = elem // self.tamanio
            else:
                 columna = elem % self.tamanio
                 fila = elem // self.tamanio + 1

        # Se ha elegido una casilla desocupada:
        else:
            fila = destiRow
            columna = destiColumn
            elem = self.tamanio * (fila - 1) + columna

        self.confi[fila-1][columna-1] = ficha
        del self.tablero_restante[self.tablero_restante.index(elem)]
        self.ganar(fila-1, columna-1) # En cada movimiento hay que preguntar si
                                      # alguien ha ganado.

    def ganar(self, fila, columna):

        # Ver si hay línea horizontal:
        j = 1
        cntganar = 1  # Esta variable almacena el valor del número de casillas
                      # consecutivas que hay de la misma ficha para cada tipo de
                      # línea.
        while((columna + j) <= self.tamanio - 1 and
                self.confi[fila][columna] == self.confi[fila][columna + j]):
           j += 1
           cntganar += 1

        j = 1
        while ((columna - j) >= 0 and
                self.confi[fila][columna] == self.confi[fila][columna - j]):
            j += 1
            cntganar += 1

        if cntganar >= self.tamanio:
            self.fin_de_juego = True
            self.message_ganar = "H"



        # Ver si hay línea vertical:

        j = 1
        cntganar = 1
        while ((fila + j) <= self.tamanio - 1 and
                self.confi[fila][columna] == self.confi[fila + j][columna]):
            j += 1
            cntganar += 1

        j = 1
        while ((fila - j) >= 0 and
                self.confi[fila][columna] == self.confi[fila - j][columna]):
            j += 1
            cntganar += 1

        if cntganar >= self.tamanio:
            self.fin_de_juego = True
            self.message_ganar = "V"


        # Ver si hay línea diagonales:

        # Diagonal hacia derecha ascendente:
        j = 1
        cntganar = 1
        while ((columna + j) <= self.tamanio-1 and (fila - j) >= 0 and
                self.confi[fila][columna] == self.confi[fila - j][columna + j]):
            j += 1
            cntganar += 1

        j = 1
        while ((columna - j) >= 0 and (fila + j) <= self.tamanio - 1 and
                self.confi[fila][columna] == self.confi[fila + j][columna - j]):
            j += 1
            cntganar += 1

        if cntganar >= self.tamanio:
            self.fin_de_juego = True
            self.message_ganar = "D"

        # Diagonal hacia izquierda ascendente:
        j = 1

        cntganar = 1
        while ((columna - j) >= 0 and (fila - j) >= 0 and
               self.confi[fila][columna] == self.confi[fila - j][columna - j]):
            j += 1
            cntganar += 1

        j = 1
        while ((columna + j) <= self.tamanio - 1 and (fila + j) <= self.tamanio - 1 and
               self.confi[fila][columna] == self.confi[fila + j][columna + j]):
            j += 1
            cntganar += 1

        if cntganar >= self.tamanio:
            self.fin_de_juego = True
            self.message_ganar = "D"


    def reset(self):
         self.confi = [['' for x in range(self.tamanio)] for y in range(self.tamanio)]
         self.tablero_restante = [i for i in range(1, self.tamanio ** 2 + 1)]
         self.message_ganar = "N"
         self.fin_de_juego = False


# 'runtavbleroNR': ejecuta una partida de N en raya. Toma como atributos un objeto de tipo
# TableroNR y el nº de veces que se ejecutará la partida: 'iteraciones'.

# La función crea un fichero de salida .csv cuyo nº de filas será 'iteraciones' y la
# siguiente info:
#  Tamanio, Nº iteración , Nº tiradas totales, Motivo de ganar: H, V o D

def runtableroNR(objtablero, iteraciones, fichero):

      try:
          s = open(fichero, 'w')

      except IOError as exc:
          print(" Exception in opening file {}: {}".format(fichero,strerror(exc.errno)))

      encabezado="Tamanio,Iteracion,Ntiradas_Ganar,LineaGanadora"
      s.write(encabezado+'\n')

      for i in range(iteraciones):
            tiradas = 0
            while(not(objtablero.fin_de_juego) and tiradas < objtablero.tamanio ** 2):
                 tiradas += 1
                 choosen_row = np.random.randint(1,objtablero.tamanio + 1)
                 choosen_column = np.random.randint(1,objtablero.tamanio + 1)
                 if tiradas % 2 == 0:
                      ficha = objtablero.fichaa
                 else:
                      ficha = objtablero.fichab
                 objtablero.movimiento(ficha,choosen_row,choosen_column)

            registro = "{0:d},{1:d},{2:d},{3:s}".format(objtablero.tamanio,
                                                        i,tiradas,
                                                        objtablero.message_ganar)

            s.write(registro+'\n')


            objtablero.reset()

      try:
          s.close()
      except IOError as exc:
          print("Error in closing file: {}: {}".format(fichero,strerror(exc.errno)))

"""
'nboard_generator' simula 'it' partidas para cada tablero de tamaño desde
Nlower hasta Nupper. Sirve para generar de una sola vez los datos correspondientes
a diferentes tamaños, creando ficheros con el nombre correspondiente.

"""

def nboard_generator(Nlower,Nupper,it,fileroot):
     
    for i in range(Nlower,Nupper+1):
        objtablero = TableroNR('X','O',i)
        s = fileroot+str(i)+"_output.csv"
        runtableroNR(objtablero,it,s)



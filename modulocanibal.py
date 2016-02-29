# -*- coding: cp1252 -*-
#----------------------------------------------------------------
#                                                               #
# Nombre del archivo del script: modulocanibal.py               #
# Nombre de los autores y sus carnets:                          #
# Andrés Alonzo --> Carné: 126483                               #
# Daniel Najera --> Carné:                                 #
# Daniel Najera --> Carné:                                 #
# Propósito del programa: Modulo de funciones para el juego de  #
# misioneros y canibales                                        #
# Fecha de creación: 08/03/2010                                 #
# Fecha de modificacion: 26/02/2016                             #
#----------------------------------------------------------------

#Se definen las listas a usar y se les asigna valor a las del lado izquierdo
global barco
global canib_iz
global canib_de
global mision_iz
global mision_de
barco= []
canib_iz = ["c", "c", "c"]
canib_de = []
mision_iz = ['m', 'm', 'm']
mision_de = []
#definir el estado del juego
global fin
fin = False

def opcionSM():
	 """
	 Funcion que sube a un misionero al barco estando del lado izquierdo
	 """
	 ciclo = True
	 while ciclo: #Entrando en el ciclo
		  try:
			   if len(barco)<2: #verificando si el barco no esta lleno
				   misionero = 'm'
				   mover(misionero, mision_iz, barco) #subiendo al misionero
				   #barIZ()
				   break #sale del ciclo
			   else:
				   print ('ERROR FATAL: el barco esta lleno, solo pueden subirse dos personajes a la vez')
				   break 
		  except:
			   print ("Error: no hay misioneros por este lado")
			   break

def opcionBM():
	 """
	 Funcion que baja a un misionero del barco, estando en el lado izquierdo
	 """
	 ciclo = True
	 while ciclo: #Iniciando el ciclo
		  try:
			   if len(barco)!=0:
				   #Subir el misionero al barco
				   misionero = 'm'
				   mover_b(misionero, mision_iz, barco)
				   #barIZ()
				   #perdedor()
				   break #Se rompe el ciclo
			   else:
				   print ('ERROR: el barco esta vacio') # imprime esto si no hay nadie en el barco(len(barco) == 2)
				   break # se rompe el ciclo
		  except: # si no hay misioneros en el barco
			  print ("No hay Misioneros en el barco")
			  break # terminar el ciclo
def opcionSC():
	"""
	Funcion que sube a un canibal al barco estando del lado izquierdo
	"""
	ciclo = True
	while ciclo: #se inicia el ciclo
		#se comprueba que el barco no este lleno y luego se sube e canibal al barco
		if len(barco)<2:
			try:
				canibal = 'c'
				mover(canibal, canib_iz, barco)
				#barIZ()
				#perdedor()
				break# rompeindo el ciclobreak
			except:
				print ("No hay canibales por este lado")
				break# rompeindo el ciclobreak
		else:
			print ('ERROR FATAL: el barco esta lleno, solo pueden subirse dos personajes a la vez')
			break

def opcionBC():
	 """
	 Funcion que baja a un canibal del barco estando del lado izquierdo
	 """
	 ciclo = True
	 while ciclo: #iniciar ciclo para bajar un canibal del barco
		  try:
			   if len(barco)!=0: # comprobar que el barco no este vacio
				   canibal = 'c'
				   mover_b(canibal, canib_iz, barco)
				   #barIZ()
				   #perdedor()
				   #ganar()
				   break# rompeindo el ciclo
			   else:
				   print ('ERROR: el barco esta vacio') #imprime esto si no hay nadie en el barco
				   break# rompeindo el ciclo
		  except:
			  print ("No hay Canibales en el barco")
def barcomover():
	 """
	 Funcion que cambia la posicion del barco
	 """
	 ciclo = True
	 while ciclo: #Mover el barco a la otra orilla
		  if len(barco) != 0:
			   #barDE()
			   bp = 'derecha'
			   #perdedor()
			   #ganar()
			   return bp
		  else:
			   print ("El barco esta vacio, Quien Crees que va a remar?")
			   bp = 'izquierda'
			   return bp
			   break


def opcionSM2():
	 """
	 Funcion que sube un misionero al barco mientras este este del lado derecho
	 """
	 ciclo = True
	 while ciclo:
		  if len(barco)<2:
			   misionero = 'm'
			   try:
				   mover(misionero, mision_de, barco)
				   #barDE()
				   #ganar()
				   #perdedor()
				   break
			   except:
				   print ("No hay misioneros por este lado")
				   print (fin)
				   break
		  else:
			  print ('El barco esta lleno. No pueden subir mas personas.')
			  break


def opcionBM2():
	 """
	 Funcion que baja un misionero al barco mientras este este del lado derecho
	 """	
	 ciclo = True
	 while ciclo:
		  ganar()
		  perdedor()
		  if len(barco)!=0:
			   misionero = 'm'
			   try:
				   perdedor()
				   mover_b(misionero, mision_de, barco)
				   barDE()
				   perdedor()
				   ganar()
				   break# rompeindo el ciclo
			   except:
				   break# rompeindo el ciclo
		  else:
			  print ('El barco esta vacio. No puede bajar nadie.')
			  break# rompeindo el ciclo
def opcionSC2():
	 """
	 Funcion que sube un canibal al barco mientras este este del lado derecho
	 """
	 ciclo = True
	 while ciclo:
		  if len(barco)<='1':
			   canibal = 'c'
			   try:
				   mover(canibal, canib_de, barco)
				   barDE()
				   ganar()
				   perdedor()
				   break# rompeindo el ciclo
			   except:
				   print ("No hay canibales por este lado")
				   ganar()
				   perdedor()
				   break# rompeindo el ciclo
		  else:
			  print ('El barco esta lleno. No pueden subir mas personas.')
			  break# rompeindo el ciclo

def opcionBC2():
	 """
	 Funcion que baja un canibal al barco mientras este este del lado derecho
	 """
	 ciclo = True
	 while ciclo:
		  if len(barco)!=0:
			  canibal = 'c'
			  mover_b(canibal, canib_de, barco)
			  perdedor()
			  barDE()
			  ganar()
			  perdedor()
			  break# rompeindo el ciclo
		  else:
			  print ('El barco esta vacio. No puede bajar nadie.')
			  perdedor()
			  break# rompeindo el ciclo
def barcomover2():
	 """
	 Funcion que mueve el barco al lado izquierdo(inicial)
	 """
	 ciclo = True
	 while ciclo: #Mover el barco a la otra orilla
		  if len(barco) != 0:
			   barIZ()
			   bp = 'izquierda'
			   perdedor()
			   ganar()
			   return bp # retornando posicion del barco y rompiendo el ciclo
		  else:
			   print ("El barco esta vacio, Quien Crees que va a remar?")
			   bp = 'derecha'
			   return bp # retornando posicion del barco y rompiendo el ciclo


def mover(personaje, lista1, lista2):
	"""
	Funcion que mueve un personaje de una lista a otra.
	"""
	posicion = lista1.index(personaje)
	cambio = lista1[posicion]
	lista1.remove(cambio) # elimina el personaje de la lista uno
	lista2.append(cambio) # agrega el personaje a la lista dos


def mover_b(personaje, lista1, lista2):
	"""
	Funcion que modifica las listas para bajar un personaje del barco
	"""
	try:
		if personaje in lista2:# comprobar si el personaje esta en la lista2 o sea el barco
			lista1.append(personaje)# agregar el personaje a la lista 1 
			lista1.sort()
			lista2.remove(personaje) # eliminar el personaje de la lista 2
	except:
		print ('Error desconocido')

def barIZ():
	"""
	Funcion que muestra el barco visualmente mientras este este del lado izquierdo
	"""
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print (canib_iz,mision_iz,"\t \t \t \t \t \t \t ",canib_de,mision_de)
	print ("_______________________________!\t \t \t !_______________________________")
	print ("                                \ ", barco,"/")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print



def barDE():
	"""
	Funcion que muestra el barco visualmente mientras este este del lado derecho
	"""
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print (canib_iz,mision_iz,"\t \t \t \t \t \t \t ",canib_de,mision_de)
	print ("_______________________________!\t \t \t !_______________________________")
	print ("                                           \ ", barco,"/ ")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print
	print


def perdedor():
	 """
	 Funcion que verifica si el jugador ha perdido.
	 """
	 global fin
	 if len(mision_iz) !=0: # si el lado izquierdo tiene misioneros
		  if len(canib_iz) > len(mision_iz):
			   # si los misioneros han sido deborados
			   fin = True
			   return [True,1]
	 if len(mision_de) != 0: # si el lado derecho tiene misioneros
		  if len(canib_de) > len(mision_de):
			   # si los misioneros han sido deborados
			   fin = True
			   return [True,2]   
	 

def mostrarperder():
	 """
	 Funcion que muestra que el usuario ha perdido y luego hace que la variable fin sea verdadera 
	 """
	 print ("PERDISTE!!! ja ja ja")
			


def ganar():
	"""
	Funcion que verifica si las listas del lado derecho tienen longitud 3, si es asi entonces se indica que se ha ganado el juego
	"""
	if len(canib_de)==3 and len(mision_de)==3: # comprobar que todos esten en el lado   
		print ('HAS GANADO!!!!!!!!')
		global fin
		fin = True
		return True
	return False
	 
def jugardnuevo():
	 """
	 funcion para jugar de nuevo
	 reserea las listas y luevo muestra el barco en su estado inicial
	 """
	 global fin
	 fin = False
	 reiniciarlistas() #Devolver las listas a su estado inicial
	 barIZ() #Mostrar el estado inicial del barco
def reiniciarlistas():
	 """
	 Funcion que devuelve las listas a su estado inicial para iniciar un juego nuevo
	 """
	 #decir que las variables van a ser globales
	 global barco
	 global canib_iz
	 global canib_de
	 global mision_iz
	 global mision_de
	 # devolver las listas a su valor inicial
	 barco= []
	 canib_iz = ["c", "c", "c"]
	 canib_de = []
	 mision_iz = ['m', 'm', 'm']
	 mision_de = []
def finret():
	 return fin


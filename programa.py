# -*- coding: cp1252 -*-
#----------------------------------------------------------------
#                                                               #
# Nombre del archivo del script: canibal.py                     #
# Nombre de los autores y sus carnets:                          #
# Andrés Alonzo --> Carné: 126483                               #
# Daniel Najera --> Carné:                                 #
# Kurt --> Carné:                                 #
# Propósito del programa: Programa principal para el juego de   #
# misioneros y canibales                                        #
# Fecha de creación: 08/03/2010                                 #
#                                                               #
#----------------------------------------------------------------
import modulocanibal #importando el modulo canibal
#inicio del codigo principal


from tkinter import * # importando el modulo Tkinter para los botones graficos
class App:
	#definir el marco de botones para las acciones
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.button = Button(frame, text="Salir", fg="red", command=frame.quit )
		self.button.pack(side=LEFT)

		self.subirmb = Button(frame, text="Subir Misionero", fg="green", command=self.uno)
		self.subirmb.pack(side=LEFT)

		self.bajarmb = Button(frame, text="Bajar Misionero", fg="green", command=self.dos)
		self.bajarmb.pack(side=LEFT)

		self.subircb = Button(frame, text="Subir Canibal", fg="green", command=self.tres)
		self.subircb.pack(side=LEFT)

		self.bajarcb = Button(frame, text="Bajar Canibal", fg="green", command=self.cuatro)
		self.bajarcb.pack(side=LEFT)

		self.movbarb = Button(frame, text="Mover Barco", fg="green", command=self.barco)
		self.movbarb.pack(side=LEFT)
		self.movbarb = Button(frame, text="Reiniciar El juego", fg="blue", command=self.reiniciar)
		self.movbarb.pack(side=LEFT)
		self.w = Label(root, text="MISIONEROS Y CANIBALES - UNIVERSIDAD DEL VALLE DE GUATEMALA\nAyuda a los misioneros y a los canibales a cruzar el rio.\nPara hacer esto, utiliza los botones de arriba para subir o bajar un personaje y tambien para mover el barco\nEstos pueden subir o bajar del barco, pero el barco solo soporta a dos personas.\nAdemas, si quedan mas canibales que misioneros en un lado de la isla,\nlos misioneros seran devorados por los canibales.")
		self.w.pack()
	modulocanibal.barIZ()
	global bp # decir que bp(posision del barco) sera global y luego darle valor
	bp = 'izquierda'

	def uno(self):
		fin = modulocanibal.finret()# revisar el estado de la variable fin(True o False)
		if not fin:
			if bp == "izquierda":
				modulocanibal.opcionSM()
			elif bp== "derecha":
				modulocanibal.opcionSM2()
			if fin:
				print ("El juego ha finalizado, para jugar de nuevo clikea \"Reinicial Juego\" o \"Salir\" para abandonar el juego")
        	
	def dos(self):
		fin = modulocanibal.finret()
		if not fin:
			if bp == "izquierda":
				modulocanibal.opcionBM()
			elif bp== "derecha":
				modulocanibal.opcionBM2()
				if fin:
					print ("El juego ha finalizado, para jugar de nuevo clikea \"Reinicial Juego\" o \"Salir\" para abandonar el juego")
	def tres(self):
		fin = modulocanibal.finret()
		if not fin:
			if bp == "izquierda":
				modulocanibal.opcionSC()
			elif bp== "derecha":
				modulocanibal.opcionSC2()
				if fin:
					print ("El juego ha finalizado, para jugar de nuevo clikea \"Reinicial Juego\" o \"Salir\" para abandonar el juego")
	def cuatro(self):
		fin = modulocanibal.finret()
		if not fin:
			if bp == "izquierda":
				modulocanibal.opcionBC()
			elif bp== "derecha":
				modulocanibal.opcionBC2()
			if fin:
				print ("El juego ha finalizado, para jugar de nuevo clikea \"Reinicial Juego\" o \"Salir\" para abandonar el juego")
	def barco(self):
		global bp
		fin = modulocanibal.finret()
		if not fin:
			if bp == "izquierda":
				movbarco = modulocanibal.barcomover()
				bp = movbarco
			elif bp== "derecha":
				movbarco = modulocanibal.barcomover2()
				bp = movbarco
			if fin:
				print ("El juego ha finalizado, para jugar de nuevo clikea \"Reinicial Juego\" o \"Salir\" para abandonar el juego")
	def reiniciar(self):
			global bp
			bp = 'izquierda'
			modulocanibal.jugardnuevo()









root = Tk()
app = App(root)
root.mainloop()

#!/usr/bin/python
# -*- coding: utf-8 -*-

class Canibal(object):
	"""Clase que contiene todos las funciones canibales."""
	def __init__(self):
		#Variables globales
		self.barco_p = 0
		self.barco_c= 0
		self.barco_m = 0
		self.canib_iz = 3
		self.canib_de = 0
		self.mision_iz = 3
		self.mision_de = 0
		self.perdedor = False
		self.ganador = False
	def getValues(self,):
		self.comprobarGanador()
		return [self.barco_p,self.canib_iz,self.mision_iz,self.canib_de,self.mision_de,self.barco_c,self.barco_m]
	def setBarcoPosition(self, value):
		if (self.barco_m + self.barco_c ) > 0:
			self.barco_p = value
			self.comprobarPerdedor()
		else:
			return False
	def subirCanibal(self,):
		if self.barco_p == 0:
			if self.canib_iz >=1:
				if (self.barco_c+self.barco_m) <2:
					self.canib_iz = self.canib_iz -1
					self.barco_c = self.barco_c +1
		if self.barco_p == 1:
			if self.canib_de >=1:
				if (self.barco_c+self.barco_m) <2:
					self.canib_de = self.canib_de -1
					self.barco_c = self.barco_c +1
	def bajarCanibal(self,):
		if self.barco_p == 0:
			if self.barco_c >=1:
				self.barco_c = self.barco_c -1
				self.canib_iz = self.canib_iz +1
		if self.barco_p == 1:
			if self.barco_c >=1:
				self.barco_c = self.barco_c -1
				self.canib_de = self.canib_de +1
	def subirMisionero(self,):
		if self.barco_p == 0:
			if self.mision_iz >=1:
				if (self.barco_c+self.barco_m) <2:
					self.mision_iz = self.mision_iz -1
					self.barco_m = self.barco_m +1
		if self.barco_p == 1:
			if self.mision_de >=1:
				if (self.barco_c+self.barco_m) <2:
					self.mision_de = self.mision_de -1
					self.barco_m = self.barco_m +1
	def bajarMisionero(self,):
		if self.barco_p == 0:
			if self.barco_m >=1:
				self.barco_m = self.barco_m -1
				self.mision_iz = self.mision_iz +1
		if self.barco_p == 1:
			if self.barco_m >=1:
				self.barco_m = self.barco_m -1
				self.mision_de = self.mision_de +1
	def comprobarPerdedor(self,):
		if (self.mision_de < self.canib_de) and self.mision_de != 0:
			print("misioneros menores que canibalez Derecha")
			self.perdedor = True
		if (self.mision_iz < self.canib_iz) and self.mision_iz !=0:
			print("misioneros menores que canibalez Izquierda")
			self.perdedor = True
	def comprobarGanador(self,):
		if self.mision_de and self.canib_de == 3:
			self.ganador = True
	
				



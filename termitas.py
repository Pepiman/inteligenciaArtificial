import numpy as np
from random import randint
#from matplotlib import mpl,pyplot

# propiedades del modelo de termitas

# Altura (en celdas) de la cuadricula.
alto = 100

# Anchura (en celdas) de la cuadricula.
ancho = 150

# Tamanio de cada celda cuadrada (en pixeles).
celda = 4

# Cantidad de termitas dentro del modelo.
termitas = 200

# Proporcion de astilla en el modelo (con probabilidad de 0 a 1).
densidad = 0.8

def crearMundo(alto,ancho,densidad):

	cuadricula = np.zeros((alto,ancho))
	probabilidades_astilla = np.random.rand(alto,ancho)
	astillas = probabilidades_astilla > densidad
	cuadricula[astillas] = 1
	return(cuadricula)

mundo = crearMundo(alto,ancho,densidad)

class Termita:
	def __init__(self,posX,posY,direccion):
		self.posX = posX
		self.posY = posY
		self.direccion = direccion
		self.cargando = False


def crearTermitas(numeroTermitas,mundo):

	alto = np.shape(mundo)[0]
	ancho = np.shape(mundo)[1]
	
	# lista de termitas vacia
	termitas = []

	for i in xrange(numeroTermitas):
		termita = Termita(randint(0,alto),randint(0,ancho),randint(0,7))
		termitas.append(termita)
	return(termitas)

termitas = crearTermitas(20,mundo)

print(termitas[0].posX)




   
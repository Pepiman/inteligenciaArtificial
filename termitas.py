import numpy as np
from random import randint
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

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

grid = crearMundo(alto,ancho,densidad)

class Termita:
	
	def __init__(self,posX,posY,direccion):
		self.posX = posX
		self.posY = posY
		self.direccion = direccion
		self.cargando = False

	def moverTermita(self):
		direcciones = np.array([7,0,1,2,3,4,5,6,7,0])
		
		'''
		Constructor de una termita
        @param posX Indica su posicion en el eje X
        @param posX Indica su posicion en el eje Y
        @param direccion Indica la direccion en la que mira.
            -----------
           | 0 | 1 | 2 |
           |-----------|
           | 7 |   | 3 |
           |-----------|
           | 6 | 5 | 4 |
            -----------
      	'''



def crearTermitas(numeroTermitas,mundo):

	alto = np.shape(mundo)[0]
	ancho = np.shape(mundo)[1]
	
	# lista de termitas vacia
	termitas = []

	for i in xrange(numeroTermitas):
		termita = Termita(randint(0,alto),randint(0,ancho),randint(0,7))
		termitas.append(termita)
	return(termitas)

def update(data):
	global grid
	newGrid = grid.copy()

	# actualizar la 'grid' global 
	newGrid = crearMundo(alto,ancho,densidad)

	mat.set_data(newGrid)
	grid = newGrid
	return [mat]

termitas = crearTermitas(20,grid)

print(termitas[0].posX)

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()




   
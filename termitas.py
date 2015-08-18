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
densidad = 0.7

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

	def aleatorizarDireccion(self):
		self.direccion = randint(0,7)

	def moverTermita(self,mundo):
		direcciones = np.array([7,0,1,2,3,4,5,6,7,0])

		opciones = direcciones[np.array([self.direccion,self.direccion+1,self.direccion+2])]

		paso_aleatorio = opciones[randint(0,2)]

		logro_moverse=False

		if paso_aleatorio == 0:
			if (self.posX-1 > 0) & (self.posY+1 < np.shape(mundo)[1]):
				self.posX = self.posX-1
				self.posY = self.posY+1
				logro_moverse=True
		elif paso_aleatorio == 1:
			if self.posY+1 < np.shape(mundo)[1]:
				self.posY = self.posY+1
				logro_moverse=True
		elif paso_aleatorio == 2:
			if (self.posX+1 < np.shape(mundo[0])) & (self.posY+1 < np.shape(mundo)[1]):
				self.posX = self.posX+1
				self.posY = self.posY+1
				logro_moverse = True
		elif paso_aleatorio == 3:
			if self.posX+1 < np.shape(mundo)[0]:
				self.posX = self.posX+1
				logro_moverse=True
		elif paso_aleatorio == 4:
			if (self.posX+1 < np.shape(mundo)[0]) & (self.posY-1 > 0):
				self.posX = self.posX+1
				self.posY = self.posY-1
				logro_moverse=True
		elif paso_aleatorio == 5:
			if self.posY-1 > 0:
				self.posY = self.posY-1
				logro_moverse=True
		elif paso_aleatorio == 6:
			if (self.posX-1 > 0) & (self.posY-1 > 0):
				self.posX = self.posX-1
				self.posY = self.posY-1
				logro_moverse=True
		elif paso_aleatorio == 7:
			if self.posX-1 > 0:
				self.posX = self.posX-1
				logro_moverse=True

		if logro_moverse == False:
			self.aleatorizarDireccion()

	def recogerAstilla(self,mundo):
		tiroAstilla = False
		direcciones_contrarias = np.array([4,5,6,7,0,1,2,3])
		if (mundo[self.posX,self.posY]==1) & (self.cargando == False):
			self.cargando=True
		elif (mundo[self.posX,self.posY]==1) & (self.cargando == True):
			self.direccion = direcciones_contrarias[self.direccion]
			self.moverTermita(mundo)
			tiroAstilla = True
		return(tiroAstilla)

	
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
		termita = Termita(randint(0+50,alto-50),randint(0+50,ancho-50),randint(0,7))
		termitas.append(termita)
	return(termitas)


# generar el mundo 
mundo = crearMundo(alto,ancho,densidad)

# crearTermitas
termitas = crearTermitas(10,mundo)

# simulacion 2 
def update(data):
	global mundo
	global termitas
	newMundo = mundo.copy()
	newTermitas = list(termitas)

	for i in xrange(len(termitas)):
		termita = termitas[i]
		
		newMundo[termita.posX,termita.posY]=2

		tiroAstilla=termita.recogerAstilla(newMundo)
			
		if termita.cargando==True:
			newMundo[termita.posX,termita.posY]=3

		if tiroAstilla==True:
			newMundo[termita.posX,termita.posY]=1

		termita.moverTermita(newMundo)

		newTermitas[i]=termita

	mat.set_data(newMundo)
	#mundo = newMundo
	termitas = newTermitas
	return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(mundo)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)

plt.show()




   
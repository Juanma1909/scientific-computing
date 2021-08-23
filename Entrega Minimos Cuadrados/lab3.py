import numpy as np
import matplotlib.pyplot as plt
from time import time
def superior(a,b): #función de sistemas triangulares superiores
	"""
	Entrada: el parametro "a" hace referencia a una matriz nxn que tiene la forma de matriz superior, la cual es la que se pretende resolver
			con el metodo de sustitucion sucesiva hacia atras, b es un arreglo [0...n]. 
	Salida: un arreglo solve[0...n] donde for solve[i] = xi donde 0 <= i < n
	Funcionamiento: en esta implementacion se pretende realizar una sucesion sucesiva hacia atrás
					donde en primer lugar se como la formula a remplazar por cada xi simepre se tiene
					bi - sumatoria, se añade a solve cada valor de bi, posteriormente se haya el valor xn
					y con base en eso se realiza la sumatoria en donde en cada solve[i] se va acumulando el valor
					que le coresponde, esto se realiza desde i = n-2 (por notacion de python) hasta 0.
	"""
	n = len(a[0])
	solve =[b[i] for i in range(n)]
	solve[n-1] = b[n-1]/a[n-1][n-1]
	i = n-2
	while i >= 0:
		for j in range(i+1,n):
			solve[i] = solve[i] - (a[i][j]*solve[j])
		solve[i] = solve[i]/a[i][i]
		i -=1
	return solve

def inferior(a,b): #función de sistemas triangulares inferiores
	n = len(b)
	solve =[b[i] for i in range(n)]
	solve[0] = b[0]/a[0][0]
	for i in range(1,n):
		for j in range(i):
			solve[i] = solve[i] - (a[i][j]*solve[j])
		solve[i] = solve[i]/a[i][i]
	return solve



def ferror(coef,t,y):
	"""
	Entrada: Un arreglo coef, el cual hace referencia a los coeficientes del polinomio de ajuste en cuestion, un arrelgo
			 t y un arreglo "y" los cuales son los datos con los que se piensa verificar el error del polinomio de ajuste
	Salida: Un arreglo errores, el cual son todos los errores absolutos obtenidos para cada valor de t
	Funcionamiento: Se crea un arreglo vacion errores, posteriormenete para cada uno de los valores en t se inyecta dicho valor
					valor en el polinomio de ajuste para así obtener el valor de este, luego se halla la diferencia con respecto
					al valor obtenido y el que está en y, el valor absoluto de dicha diferencia se almacena en el arreglo errores

	"""
	errores = []
	n,m = len(coef),len(t)
	for j in range(m):
		val = 0
		for i in range(n):
			val+= coef[i]*pow(t[j],i)
		errores.append(abs(val-y[j]))			
	return errores

def perror(mean,devia):
	"""
	Entrada: mean es un valor numerico que hace referencia al error medio con respecto a las evaluaciones,
			 devia hace referencia la desviacion estandar (standard deviation en inglés)
	Salida:  Una impresion más organizada de el error medio y la desviacion estandar
	Funcionamiento: lo que se hace es imprimir 2 lineas de texto, una que contiene "Error Medio:" seguido de su
					valor numerico correspondiente, y la otra que contiene "Desviacion Estandar:" seguido de su 
					valor numerico correspondiente.
	"""
	print("Error Medio: " + str(mean))
	print("Desviacion Estandar: " + str(devia))
	return


def plotpoly(t,coef):
	"""
	Entrada: un arreglo t de tiempos, y un arreglo coef de coeficientes los cuales hacen alusion a los coeficientes
			 del polinomio de ajuste
	Salida:  un arrelgo x que hace referencia al conjunto de puntos en el eje X para grafical el polinomio, y un arreglo y
			 el cual hace referncia al conjunto de imagenes de las evaluciaones de x en el polinomio de ajuste a traves de 
			 los coeficientes
	Funcionamiento: Haciendo uso de linspace se crea todos los puntos en el eje X basandose como cota inferior el primer elemento de t,
					y como cota superior el ultimo elemento en t, siendo estos un totol de 200 puntos. Posteriormente se evalua el
					polinomio de ajuste con respecto a arreglo x 
	"""
	x = np.linspace(t[0],t[-1],200)
	n = len(coef)
	y = 0
	for i in range(n):
		y+= coef[i]*pow(x,i)

	return x,y

def SepValues(t,b):
	"""
	Entrada: Un arreglo t que hace referencia al tiempo, y un arreglo b que hace referencia a los valores en el eje y correspondientes
			 a cada valor en el arreglo t
	Salida: 4 arreglos tTrain,tVal, yTrain, yVal los cuales hacen referencia a la separacion de los datos en aquellos de entrenamiento
			(tTrain y yTrain) y los de validacion (tVal y yVal)
	Funcionamiento: Se hace un recorrido por todas las posiciones de los arreglos y aquellos valores en posiciones pares van al grupo
				 	de entrenamiento, y los que esten en impares van a grupo de validacion.
	"""
	n = len(t)
	tTrain,tVal, yTrain, yVal = [],[],[],[]
	for i in range(n):
		if i%2 == 0:
			tTrain.append(t[i])
			yTrain.append(b[i])
		else:
			tVal.append(t[i])
			yVal.append(b[i])
	return tTrain,tVal, yTrain, yVal

def Householder(g,t,b):
	"""
	Entrada: un numero p perteneciente a los naturales positivos, el cual hace referencia a la cantidad de parametros
			 que tendría el polinomio de ajuste, un arreglo t donde for all i,j where i < j | t[i] < t[j], por ultimo 
			 llega un arreglo b el cual hace referencia a los valores en el eje "y", correspondientes al arreglo t.
	Salida: la funcion retorna un arreglo coef el cual es el conjunto de coeficientes correspondientes al polinomio de ajuste obtenido 
			a traves de metodo de transformaciones householder, de igual manera retorna un arreglo x de 200 posiciones y un arreglo "y" de 200
			posiciones los cuales son utilizados para graficar el polinomio de ajuste obtenido. esto 2 arreglos se crean a traves de la
			funcion plotpoly
	Funcionamiento: En primer lugar teniendo el tamaño de t y la cantidad de parametros del polinomio de ajuste, se crea la matriz A, posteriormente
					se itera por cada columna, en cada iteracion se halla el vector v correspondiente haciendo uso de la norma de la columna en cuestion,
					de ahí se pasa a hallar la matris H a traves de la formula vista en clase. Finalmente se multiplica la matriz A por la H hasta quedar
					con un sistema triangular superior y este se resuleve haciendo uso de sutitucion sucesiva hacia atras.
	"""
	n = len(t)
	A = [[None for _ in range(g+1)] for _ in range(n)]
	for i in range(n):
		for j in range(g+1):A[i][j] = pow(t[i],j)
	col = len(A[0])	
	fil = len(A)
	m = np.identity(fil)
	for i in range(col):		
		v = [0 for _ in range(fil)]
		a = [0 for _ in range(fil)]
		for j in range(i,fil):
			a[j]=A[j][i]
		norm = np.linalg.norm(a)
		v[i] = norm
		if a[i]*v[i] > 0: v[i] = -1*v[i]		
		aux = np.subtract(a,v)
		v = np.zeros((fil,1))
		for h in range(i,fil):
			v[h][0] = aux[h]
		vt = np.transpose(v)		
		ar = np.matmul(v,vt)		
		ab = np.matmul(vt,v)				
		c = 2*(ar/ab)
		h = np.subtract(m,c)		
		A = np.dot(h,A)
		b = np.matmul(h,b)		
	coef= superior(A,b)
	#print("Coefficients = ")
	#print(coef)
	x,y = plotpoly(t,coef)		
	return x,y,coef


def Ecn(g,t,b):
	"""
	Entrada: un numero p perteneciente a los naturales positivos, el cual hace referencia a la cantidad de parametros
			 que tendría el polinomio de ajuste, un arreglo t donde for all i,j where i < j | t[i] < t[j], por ultimo 
			 llega un arreglo b el cual hace referencia a los valores en el eje y correspondientes al arreglo t
	Salida: la funcion retorna un arreglo coef el cual es el conjunto de coeficientes correspondientes al polinomio de ajuste obtenido 
			a traves de metodo de ecuaciones normales, de igual manera retorna un arreglo x de 200 posiciones y un arreglo "y" de 200
			posiciones los cuales son utilizados para graficar el polinomio de ajuste obtenido. esto 2 arreglos se crean a traves de la
			funcion plotpoly
	Funcionamiento: En primer lugar teniendo el tamaño de t y la cantidad de parametros del polinomio de ajuste, se crea la matriz A,
					posteriormente usando numpy se obtiene la matriz transpuesta de A llamada At, luego se multiplican ambas matrices
					y se multiplica tambien el vector b por At, finalmente se utiliza la descomposicion de cholesky para obtenr las matrices
					L y  L1, usando los metodos se sustitucion sucesiva correspondientes se resulven los sistemas triangulares resultantes,
					utilizando el  resultado de L como entrada para resolver L1. finalmente ya teniendo los coeficientes se hace uso de la
					funcion plotpoly para obtener la imagens y preimagens de polinomio de ajuste resultante.
	"""
	n = len(t)
	A = [[None for _ in range(g+1)] for _ in range(n)]
	for i in range(n):
		for j in range(g+1):A[i][j] = pow(t[i],j)	
	At = np.transpose(A)
	Aa = np.dot(At,A)
	bb = np.dot(At,b)	
	L = np.linalg.cholesky(Aa)
	L1 = np.transpose(L)	
	y = inferior(L,bb)
	#print("Y = ")
	#print(y)
	coef = superior(L1,y)
	#print("Coefficients = ")
	#print(coef)
	x,y = plotpoly(t,coef)


	return x,y,coef

def main():
	timeStart = time()
	g = 11
	t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7]
	y = [3624, 3644, 3666, 3658, 3653, 3640, 3669, 3703, 3694, 3739, 3731, 3752, 3739, 3773, 3803, 3786, 3788, 3767, 3782, 3778, 3763, 3777, 3796, 3803, 3799, 3795, 3805, 3848, 3859, 3888, 3881, 3850, 3837, 3767, 3741, 3691, 3696, 3723, 3717, 3773, 3739, 3716, 3726, 3723, 3704, 3720, 3729, 3739, 3802, 3841, 3875, 3908, 3893, 3887, 3896, 3907, 3858]
	tTrain,tVal, yTrain, yVal = SepValues(t,y) # Se separan los valores en validacion y entrenamiento
	print("Ecuaciones Normales")
	EcnStart = time()
	xEcn,yEcn,EcCoef = Ecn(g,tTrain,yTrain)
	#Hallan elos errores absolutos error medio y desviacion estandar
	EcnErr = ferror(EcCoef,tVal,yVal)
	EcnMeanEr = np.mean(EcnErr)
	EcnStd = np.std(EcnErr)
	perror(EcnMeanEr,EcnStd)
	EcnTotal = time() - EcnStart #Se evalua el timepo que tomo ejecutar el algoritmo de Ecuaciones Normales
	print()
	print("Transformaciones Householder")
	HHStart = time()
	xHH,yHH,HHCoef = Householder(g,tTrain,yTrain)
	#Hallan elos errores absolutos error medio y desviacion estandar
	HHErr = ferror(HHCoef,tVal,yVal)
	HHmeanEr = np.mean(HHErr)
	HHStd = np.std(HHErr)
	perror(HHmeanEr,HHStd)
	HHTotal = time() - HHStart #Se evalua el timepo que tomo ejecutar el algoritmo de Transformaciones Householder
	print()
	print("Tiempos de Ejecucion")
	print("Transformaciones Householder: " + str(HHTotal))
	print("Ecuaciones Normales: " + str(EcnTotal))
	plt.plot(xHH,yHH, label = "Householder Transformations")
	plt.plot(xEcn, yEcn, label = "Normal Ecuations")
	plt.plot(tTrain, yTrain, 'o', label = "Puntos de Entrenamiento")
	plt.plot(tVal,yVal, 'o', label = "Puntos de Validacion")
	plt.title("Grafica Comparativa")
	plt.xlabel("Dias")
	plt.ylabel("Precio Maximo del Dolar") #comentar esta linea para la base de datos 1
	#plt.ylabel("Casos confirmados de Covid 19 en el Meta") descomentar esta linea para la base de datos 1
	plt.legend()
	plt.show() #Graficar
	return
main()

"""
tBase1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4]
yBase1 = [1,1,1,2,2,1,4,1,1,1,1,2,1,1,1,17,1,2,2,5,10,5,20,30,5,21,11,24,24,44,19,14,89,4,26,84,6,85,1,195,5,20,77,68,3,8,2,4,2,4,2,11,1,2,1,1,3,1,5,5,3,2,2,3,1,4,2,5,4,21,8,10,5,9]
tBase2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7]
yBase2 = [3624, 3644, 3666, 3658, 3653, 3640, 3669, 3703, 3694, 3739, 3731, 3752, 3739, 3773, 3803, 3786, 3788, 3767, 3782, 3778, 3763, 3777, 3796, 3803, 3799, 3795, 3805, 3848, 3859, 3888, 3881, 3850, 3837, 3767, 3741, 3691, 3696, 3723, 3717, 3773, 3739, 3716, 3726, 3723, 3704, 3720, 3729, 3739, 3802, 3841, 3875, 3908, 3893, 3887, 3896, 3907, 3858]
"""

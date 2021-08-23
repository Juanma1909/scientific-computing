import matplotlib.pyplot as plt
import numpy as np
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
	print("Desviación Estándar: " + str(devia))
	return

def inferior(a,b): #función de sistemas triangulares inferiores
	n = len(b)
	solve =[b[i] for i in range(n)]
	solve[0] = b[0]/a[0][0]
	for i in range(1,n):
		for j in range(i):
			solve[i] = solve[i] - (a[i][j]*solve[j])
		solve[i] = solve[i]/a[i][i]
	return solve

def printm(a):
	for x in a:print(x)
	print()
	return

def ferror(coef,t,y):
	"""
	Entrada: Un arreglo coef, el cual hace referencia a los coeficientes del polinomio de ajuste en cuestion, un arrelgo
			 t y un arreglo "y" los cuales son los datos con los que se piensa verificar el error del polinomio de ajuste
	Salida: Un arreglo errores, el cual son todos los errores absolutos obtenidos para cada valor de t
	Funcionamiento: Se crea un arreglo vacio errores, posteriormenete para cada uno de los valores en t se inyecta dicho valor
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

def ftrerror(coef,t,y,c):
	"""
	Entrada:un arreglo coef de tuplas, en la que cada tupla contiene el m y el b correspondintes a la recta	de trozo en cuestion,
			un arreglo t y un arreglo "y" los cuales son los datos con los que se piensa verificar el error del polinomio, y un entero C que
			ayuda a determinar en qué trozo se encuentra el punto de validacion
	Salida:Un arreglo errores, el cual son todos los errores absolutos obtenidos para cada valor de t
	Funcionamiento:Se crea un arreglo vacio errores, posteriormenete se hace un ciclo en el que en cada iteración se detrmina el trozo al que pertence
	 			   el t en cuestion, se inyecta dicho valor en el polinomio del trozo correspondiente para así obtener el valor de este, luego se
	 			   halla la diferencia con respecto	al valor obtenido y el que está en y, el valor absoluto de dicha diferencia se almacena en el arreglo errores
	"""
	c -=1
	n = len(t)
	j = 0	
	errores = []
	for i in range(n):		
		if i%c == 0: j+=1
		if j < len(coef):
			#print("i {0} j {1}".format(i,j))
			val = (coef[j][0]*t[i]) + coef[j][1]
			errores.append(abs(val - y[i]))
	return errores

def newtferror(t,y,x,coef):
	"""
	Entrada:Un arreglo x y un arreglo "y" los cuales son los datos con los que se piensa verificar el error del polinomio, un arreglo t de donde
			se obtienen lo valores a restar en la productorio (t-t1)(t-t2)..., y un arreglo coef, el cual hace referencia a los x por los que se multiplica cada
			término del polinomio
	Salida:Un arreglo errores, el cual son todos los errores absolutos obtenidos para cada valor de t, un arre
	Funcionamiento:Se crea un arreglo errores vacio, porteriormente para cada uno de los valores en x se inyecta dicho valor en el polinomio de newton, se evaluo el polinomio
				   creando las dintias productorias dependiendo del termino que se esté evaluando, al final de la productoria se multiplica el resultao por el coeficiente del
				   término en cuestion,luego se	 			   halla la diferencia con respecto	al valor obtenido y el que está en y, el valor absoluto de dicha
				   diferencia se almacena en el arreglo errores
	"""
	n = len(t)
	m = len(x)
	errores = []	
	for a in range(m):
		tmp = 1
		acum = 0
		for i in range(n):
			if i != 0:
				tmp = tmp*(x[a]-t[i-1])			
			acum += coef[i]*tmp
		errores.append(abs(acum-y[a]))
	return errores

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
	
def SepValues(t,b,c):
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
		if i%c == 0:
			tTrain.append(t[i])
			yTrain.append(b[i])
		else:
			tVal.append(t[i])
			yVal.append(b[i])
	return tTrain,tVal, yTrain, yVal

def trozos(t,y):
	"""
	Entrada:un arreglo t y un arreglo y los cuales hacen refencia a los valores de entrenamiento para generar la interpolacion
	Salida: un arreglo ans el cual es un arreglo de tuplas en la que cada tupla contiene el valor m y el valor b de la ecuacion y = mx + b
			de cada uno de los trozos 
	Funcionamiento:Se realiza un ciclo en el que en cada una de las iteraciones se toman los 2 valores ectremos del troo que se va a evaluar (t[i] y t[i+1])
				   utilizando esos 2 puntos se resulve la ecuacion de la recta y = mx + b hallando m como la razon entre el cambio en y y el cambio en x, y se
				   halla b reemplazando uno de los puntos en la ecuacion y despejando, luego se evalua la ecuacion encontrada en los x que recibe la funcion
				   y se grafica el resultado, po rultimo se guarda la razon de cambio y el y-intercepto en el arreglo ans
	"""
	n = len(t)
	ans = []
	for i in range(n-1):
		x = np.linspace(t[i],t[i+1],100)
		#print("[{0} {1}]".format(t[i],t[i+1]))
		m = (y[i]-y[i+1])/(t[i]-t[i+1])
		b = y[i] - m*(t[i])
		yTemp = m*x + b
		ans.append((m,b))
		plt.plot(x,yTemp,'r') # funcion trozos
	return ans

def newton(t,b,x):
	"""
	Entrada:un arreglo t y un arreglo y los cuales hacen refencia a los valores de entrenamiento para generar la interpolacion, un arreglo x
			el cual es un linspace, este es utilizado para podre graficar el polinomio
	Salida:un arreglo ans el cual hace referencia a los valores en el eje y evaluados en x, y un arreglo coef el cual hace refencia a los valores
		   Xi de cada uno de los terminos del polinomio de newton
	Funcionamiento: Se crea una matriz cuadrada A, posteriormente la matriz se recorre de manera triangular en la que cada celda es la multiplicaion
					de la celda anterior a esta por la diferencia enre un par de valores encontrados en t, la matris A resultante es triangular
					por lo que se usa sustitucion sucesiva hacia adelante para poder obtener los valores Xi del polinomio, finalmente por cada valor 
					dentro del linspace x se evalua el polinomio a traves de la solucion de la productoria y la multiplicaion de cada término por su
					xi correspondiente, el resultado se guarda en ans.
	"""
	n = len(t)
	A = [[0 for _ in range(n)] for _ in range(n)]
	#printm(A)
	ans = 0
	for i in range(n):		
		for j in range(i+1):			
			if j == 0: A[i][j]= 1
			else:				
				A[i][j] = float(A[i][j-1]) * (t[i]-t[j-1])
	coef = inferior(A,b)
	#print(coef)

	ans =[]
	for a in x:
		tmp = 1
		acum = 0
		for i in range(n):
			if i != 0:
				tmp = tmp*(a-t[i-1])			
			acum += coef[i]*tmp
		ans.append(acum) 	
	return ans,coef 

def Householder(g,t,b):
	"""
	Entrada: un numero g perteneciente a los naturales positivos, el cual hace referencia a la cantidad de parametros
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
	x,y = plotpoly(t,coef)		
	return x,y,coef

def lagrange(A,b,t):
	'''
	Entrada: Recibe un arreglo Ax[0...n] y un arreglo b[0...n] donde n es la longitud
	de los arreglos y un t, que sería una lista de tiempos a evaluar.
	Salida: Retorna puntos a graficar dado por los t en cuestión.
	Funcionamiento: Recorre el tamaño de las listas de manera tal que se pueda realizar
	la formula dada para lagrange.
	'''
	A = np.array(A)
	n = len(A)
	ans = 0
	for i in range(n):
		acum1 = 1
		acum2 = 1
		for j in range(n):
			if i != j:
				acum1 *= t - A[j]
				acum2 *= A[i]-A[j]
		x = b[i]*(acum1/acum2)
		ans += x
	return ans

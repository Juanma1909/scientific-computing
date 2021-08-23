import numpy as np

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
	n = len(b)
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
	
def solveGJ(a,b):
	"""
	Entrada:el parametro "a" hace referencia a una matriz nxn, la cual al haber sido ya
	procesada con anterioridad tiene una forma de matriz diagonal, b es un vector de n filas 
	Salida: un arreglo solve [0...n] en el que solve[i] = xi where 0 <= i < n
	Funcionamiento: al ser una matriz diagonal quiere decir que cada fila tiene sólo un coeficiente
					por lo que, basta con realizar un ciclo que divida b[i] entre a[i][i] para
					asi poder obtener el valor de xi whre 0 <= i < n
	"""
	n = len(b)
	solve = [0 for _ in range(n)]
	for i in range(n):
		solve[i] = b[i]/a[i][i]
	return solve


def GaussJ(a,b):
	"""
	Entrada:Una matriz "a" nxn, y un arreglo b [0...n] el cual hace referencia a un vector
	Salida: una matriz diagonal "a",la cual es enviada a la funcion SolveGJ para poder obtener
			todas las distintas soluciones xi where 0 <= i < n
	Funcionamiento: en primer lugar se define col, como la columna donde empieza el proceso de 
					aniquilacion, se crea una matriz identidad a traves de la librería numpy,
					se escoje un pivote y se verifica que su valor se diferente de 0, una vez hecho
					esto se procede a crear la matriz de eliminacion que permite aniquilar una columna,
					este proceso continua hasta que no hayan más columnas por aniquilar. si en algun punto
					se escoge un pivote con valor 0, se procede a hacer una permutacion entre filas, verficando
					que el pivote en la fila seleccionada sea distinto de 0.
	"""
	n = len(b)
	col = 0
	while col < n:
		#printm(a)
		pv = a[col][col]
		m = np.identity(n)
		if pv == 0 and col != n-1:
			stop = False
			t = col+1
			while not(stop) and t < n:
				if a[t][col] != 0:
					temp =list(a[col])
					a[col] = list(a[t])
					a[t] = temp
					tempb = b[col]
					b[col] = b[t]
					b[t] = tempb
					stop = True
					pv = a[col][col]
				t+=1
		for i in range(n):
			if i != col:
				m[i][col] = -1*(a[i][col]/pv)
		a = np.dot(m,a)
		b = np.dot(m,b)
		col+=1
	return solveGJ(a,b)

def Gauss(Ax, b):
	"""
	Entrada: Recibe una matriz "a" nxn y un arreglo b[0...n]
	Salida: Retorna la solución de Gauss."""
	n = len(Ax)
	col = 0
	while(col != n-1):
		m = np.identity(n) #matriz identidad
		pv = Ax[col][col] #pivote
		if pv == 0 and col != n-1:
			stop = False
			t = col+1
			while not(stop) and t < n: #se recorren las filas para escoger la fila a permutar
				if Ax[t][col] != 0:
					temp =list(Ax[col])
					Ax[col] = list(Ax[t])
					Ax[t] = temp
					tempb = b[col]
					b[col] = b[t]
					b[t] = tempb
					stop = True
					pv = Ax[col][col]
				t+=1
		aux = [Ax[i][col] for i in range(n)]
		for i in range(col+1,n): #crea la matriz Mi
			m[i][col] = -1*(aux[i]/pv) #operación de dividir los elementos de la col con el pivote
		McolA = np.dot(m,Ax) #multiplicación de matrices la cual da la aniquilación
		McolB = np.dot(m,b) #multiplicación de la matriz Mi con el b.
		Ax = McolA # actualización de los nuevos resultados
		b = McolB # actualización de los nuevos resultados
		col+=1 #se aumenta el número de columna
	ans = superior(Ax,b) #funcion que retorna el resultado.
	return ans

def main():
	a,b = [[1,1,1],[1,1,2],[2,3,5]],[400,600,1500]
	det = np.linalg.det(a)
	if det == 0:
		print("Es una matriz singular")
	else:
		print("No es una matriz singular")
		print("Gauss:")
		solve = Gauss(a,b)
		for x in range(len(solve)):
			print("x" + str(x+1) + ": " + str(round(solve[x],4)))
		print("Gauss-Jordan:")
		solve = GaussJ(a,b)
		for x in range(len(solve)):
			print("x" + str(x+1) + ": " + str(round(solve[x],4)))
	#EJEMPLOS
	AxS = [[0,9,-2],[0,4,1],[0,1,4]] # Matriz singular
	AxG = [[5,4,-1,2,-9],[4,3,-5,-5,4],[6,-6,-3,-9,4],[-8,8,5,-3,-6],[-3,-7,2,-5,4]] #ejemplo extra para gauss
	bG = [29,-65,-113,35,-50]
	a0,b0 = [[0,9,-2],[0,4,1],[4,1,4]],[2,4,8]#ejemplo pivote 0
main()

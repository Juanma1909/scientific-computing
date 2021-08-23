import numpy as np
import matplotlib.pyplot as plt
from time import time

def printA(f,x):
	"""
	Entrada: una funcion f y un arreglo x de números reales
	Salida: un arreglo y de numeros reales correspondientes a la evaluacion de f(x)
	Funcionamiento: se realiza un ciclo iterando por cada valor dentro del arreglo x, en cada iteracion
					se evalua dicho valor en la función f y su resultado se almacena en el arreglo y
	"""
	y = []
	for a in x:
		ans = f(a)
		y.append(ans)
	return y

def printD(met,x,h,f):
	"""
	Entrada: un metodo met, un arreglo x de numeros reales, un numero h y un funcion f
	Salida: un arrelgo correspondiente a la evaluación del metodo escogido con el h y un valor
			perteneciente a x
	Funcionamiento: se realiza un ciclo iterando por cada valor dentro del arreglo x, en cada iteracion
					se evalua dicho valor en la metodología met con la función f y el h determinado, el
					resultado se almacena en el arreglo y
	"""
	y = []
	for a in x:
		ans = met(f,a,h)
		y.append(ans)
	return y

def errores(yReal, yAT,yAD,yCE):
	"""
	Entrada: 4 arreglos de numeros reales yReal, yAT, yAD y yCE el primero hace referencia a los valores
			obtenidos con la derivada analitica y los utlimos 3 hacen referencia a los valores obtenidos 
			mediante los metodos diferecias finitas hacia atras,adelante y centrada respectivamente
	Salida: 3 arreglos de numeros reales los cuales hacen referencia a los errores absolutos de los metodos
			diferecias finitas hacia atras,adelante y centrada respectivamente  
	Funcionamiento: se realiza un ciclo iterando por cada valor dentro del arreglo yReal, en cada iteracion
					halla la diferencia absoluta con respecto a cada método, posteriormente dicahas diferencias se almacenan
					en su arreglo a retornar correspondiente
	"""
	n = len(yReal)
	ErAT,ErAD,ErCE = [],[],[]
	for i in range(n):
		ErAT.append(abs(yReal[i] - yAT[i]))
		ErAD.append(abs(yReal[i] - yAD[i]))
		ErCE.append(abs(yReal[i] - yCE[i]))
	return ErAT,ErAD,ErCE

def ptime(tAD,tAT,tCE):
	"""
	Entrada: 3 tiempos de ejecución tAD,tAT y tCE los cuales hacen referencia a los tiempos de ejecucion
			de los metodos diferecias finitas hacia adelante,atras y centrada respectivamente
	Salida: se muestra en cosola los tiempos en cuestión
	Funcionamiento: se realiza un print de los tiempos
	"""
	print("Tiempos de ejecucion:")
	print("Adelante: " + str(tAD))
	print("Atras: " + str(tAT))
	print("Centrado: " + str(tCE))
	return



def perror(err):
	"""
	Entrada: err es un arreglo que hace referencia a los errores absolutos de uno de los metodos.
	Salida:  Una impresion más organizada de el error medio y la desviacion estandar
	Funcionamiento: primero se halla tanto el error medio como la desviacion estandar de los errores absolutos 
					posteriormente lo que se hace es imprimir 2 lineas de texto, una que contiene "Error Medio:" seguido de su
					valor numerico correspondiente, y la otra que contiene "Desviacion Estandar:" seguido de su valor numerico correspondiente.
	"""
	mean = np.mean(err)
	devia = np.std(err)
	print("Error Medio: " + str(mean))
	print("Desviación Estándar: " + str(devia))
	return


"""
Este grupo de funciones hacen referencia a las funciones reales y sus derivadas analiticas correspondientes,
estas reciben un numero real x y retornal el valor de su imagen, de acuerdo a la evaluacion que se realice,
para su creacin se hizo uso de la librería numpy
"""
def seno2(x): return np.sin(2*x)

def logaritmo(x): return np.log(x)

def expo2(x): return np.exp(2*x)

def devseno2(x): return 2*np.cos(2*x)

def devlog(x): return 1/x

def devexpo2(x): return 2*np.exp(2*x)

def derAtras(f,x,h):
	"""
	Entrada:Una funcion f,un valor h y un valor x
	Salida: el valor aporximado de la derivada de la funcion f a traves del metodo en cuestion
	Funcionamiento: Se toman los valores de x y h y se evaluan con respecto a lo que dicta el 
					metodo de Diferencias finitas hacia atras
	"""
	ans = f(x) - f(x-h)
	ans = ans/h
	return ans

def derAdelante(f,x,h):
	"""
	Entrada:Una funcion f,un valor h y un valor x
	Salida: el valor aporximado de la derivada de la funcion f a traves del metodo en cuestion
	Funcionamiento: Se toman los valores de x y h y se evaluan con respecto a lo que dicta el 
					metodo de Diferencias finitas hacia adelante
	"""
	ans = f(x+h) - f(x)
	ans=ans/h
	return ans

def derCentro(f,x,h):
	"""
	Entrada:Una funcion f,un valor h y un valor x
	Salida: el valor aporximado de la derivada de la funcion f a traves del metodo en cuestion
	Funcionamiento: Se toman los valores de x y h y se evaluan con respecto a lo que dicta el 
					metodo de Diferencias finitas centrada
	"""
	ans = f(x+h)-f(x-h)
	ans = ans/(2*h)
	return ans

	
def main():
	"""
	en la funcion main se realiza un for donde en cada iteracion el valor de h se divide entre 10 y así tienda más a 0, en cada ciclo
	se hallan los valores de las derivadas aproximadas así como el valor de la derivada analitica para un conjunto de puntos x, posteriormente
	se hallan los errores medios para cada uno de los metodos, eso se hace para cada una de las funciones reales escogidas	

	"""
	x = np.linspace(0.5,10,200)
	print("Funcion Seno(2x)")
	ySinA = printA(devseno2,x)
	h = 1
	for i in range(4):
		if i != 0: h/=10
		print(str(h))
		tsAD = time()				
		ySinAD = printD(derAdelante,x,h,seno2)
		totalsAD = time() - tsAD
		tsAT = time()
		ySinAT = printD(derAtras,x,h,seno2)
		totalsAT = time() - tsAT
		tsCE = time()
		ySinCE = printD(derCentro,x,h,seno2)
		totalsCE = time() - tsCE
		errAT,errAD,errCE=errores(ySinA,ySinAT,ySinAD,ySinCE)
		perror(errAT)
		perror(errAD)
		perror(errCE)
		ptime(totalsAD,totalsAT,totalsCE)
		plt.title("Funcion Seno")		
		plt.plot(x,ySinA, label = "Derivada Analitica")
		plt.plot(x,ySinAD, label = "Adelante")
		plt.plot(x,ySinAT, label = "Atras")
		plt.plot(x,ySinCE, label = "Centrada")
		plt.grid()
		plt.legend()
		plt.show()

	print("Funcion logaritmo(x)")
	x = np.linspace(1.1,10,200)
	yLogA = printA(devlog,x)
	h = 1
	for i in range(4):
		if i != 0: h/=10
		print(str(h))
		tlAD = time()		
		yLogAD = printD(derAdelante,x,h,logaritmo)
		totallAD = time() - tlAD
		tlAT = time()
		yLogAT = printD(derAtras,x,h,logaritmo)
		totallAT = time() - tlAT
		tlCE = time()
		yLogCE = printD(derCentro,x,h,logaritmo)
		totallCE = time() - tlCE
		errAT,errAD,errCE=errores(yLogA,yLogAT,yLogAD,yLogCE)
		perror(errAT)
		perror(errAD)
		perror(errCE)
		ptime(totallAD,totallAT,totallCE)
		plt.title("Funcion Logaritmo")
		plt.plot(x,yLogA, label = "Derivada Analitica")
		plt.plot(x,yLogAD, label = "Adelante")
		plt.plot(x,yLogAT, label = "Atras")
		plt.plot(x,yLogCE, label = "Centrada")
		plt.grid()
		plt.legend()
		plt.show()

	x = np.linspace(0.5,10,200)
	print("Funcion e^(2x)")
	yEA = printA(devexpo2,x)
	h = 1
	for i in range(4):
		if i != 0: h/=10
		print(str(h))
		teAD = time()		
		yEAD = printD(derAdelante,x,h,expo2)
		totaleAD = time() - teAD
		teAT = time()
		yEAT = printD(derAtras,x,h,expo2)
		totaleAT = time() - teAT
		teCE = time()
		yECE = printD(derCentro,x,h,expo2)
		totaleCE = time() - teCE
		errAT,errAD,errCE=errores(yEA,yEAT,yEAD,yECE)
		perror(errAT)
		perror(errAD)
		perror(errCE)
		ptime(totaleAD,totaleAT,totaleCE)
		plt.title("Funcion e")
		plt.plot(x,yEA, label = "Derivada Analitica")
		plt.plot(x,yEAD, label = "Adelante")
		plt.plot(x,yEAT, label = "Atras")
		plt.plot(x,yECE, label = "Centrada")
		plt.grid()
		plt.legend()
		plt.show()
	return
main()


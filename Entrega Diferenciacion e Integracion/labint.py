import numpy as np
import matplotlib.pyplot as plt
from time import time

def seno2(x): return np.sin(2*x)

def logaritmo(x): return np.log(x)

def expo2(x): return np.exp(2*x)

def intseno2(x): return(np.cos(2*x))/-2

def intlog(x):
	ans = (x*np.log(x))
	ans = ans-x
	return ans

def intexpo2(x): return(np.exp(2*x))/2

def perror(errec,ertrap,ersimp):
	print("Error rectangulo: " + str(errec))
	print("Error trapezoide: " + str(ertrap))
	print("Error simpson: " + str(ersimp))
	return

def ptime(trec,ttra,tsim):
	"""
	Entrada: 3 tiempos de ejecución tAD,tAT y tCE los cuales hacen referencia a los tiempos de ejecucion
			de los metodos diferecias finitas hacia adelante,atras y centrada respectivamente
	Salida: se muestra en cosola los tiempos en cuestión
	Funcionamiento: se realiza un print de los tiempos
	"""
	print("Tiempos de ejecucion:")
	print("rectangulo: " + str(trec))
	print("trapezoide: " + str(ttra))
	print("simpson: " + str(tsim))
	return



def evaluar(a,b,f):
	ans = f(b) - f(a)
	return ans

def rectangulo(a,b,n,f):
	cont = (b-a)/n
	ans = 0
	while a < b:
		nex = a+cont
		ev = (a+nex)/2
		ans+=(nex - a)*f(ev)
		a+=cont
	return ans

def trapezoide(a,b,n,f):
	cont = (b-a)/n
	ans = 0
	while a < b:
		nex = a+cont
		ans +=(nex-a)*(f(nex) + f(a))
		a+=cont
	return (ans)/2

def simpson(a,b,n,f):
	cont = (b-a)/n
	ans = 0
	while a < b:
		nex = a+cont
		ev = (a+nex)/2
		ans += (nex -a)*((f(nex) + f(a))+(4*f(ev)))
		a+=cont		
	return(ans)/6



def main():
	a,b,n = 2,5,40
	print("Funcion Seno")
	real = evaluar(a,b,intseno2)
	trec = time()
	rec = rectangulo(a,b,n,seno2)
	totalr = time()-trec
	ttra = time()
	trap = trapezoide(a,b,n,seno2)	
	totalt=time()-ttra
	tsim = time()
	simp = simpson(a,b,n,seno2)
	totals=time()-tsim
	errec = abs(real - rec)
	ertr = abs(real - trap)
	ersi = abs(real - simp)
	perror(errec,ertr,ersi)
	ptime(totalr,totalt,totals)

	print("Funcion logaritmo")
	real = evaluar(a,b,intlog)
	trec = time()
	rec = rectangulo(a,b,n,logaritmo)
	totalr = time() - trec
	ttra = time()
	trap = trapezoide(a,b,n,logaritmo)
	totalt = time() - ttra
	tsim = time()
	simp = simpson(a,b,n,logaritmo)
	totals = time() - tsim
	errec = abs(real - rec)
	ertr = abs(real - trap)
	ersi = abs(real - simp)
	perror(errec,ertr,ersi)
	ptime(totalr,totalt,totals)

	print("Funcion e^(2x)")
	real = evaluar(a,b,intexpo2)
	trec = time()
	rec = rectangulo(a,b,n,expo2)
	totalr = time() - trec
	ttra = time()
	trap = trapezoide(a,b,n,expo2)
	totalt = time() - ttra
	tsim = time()
	simp = simpson(a,b,n,expo2)
	totals = time() - tsim
	errec = abs(real - rec)
	ertr = abs(real - trap)
	ersi = abs(real - simp)
	perror(errec,ertr,ersi)
	ptime(totalr,totalt,totals)



	return
main()

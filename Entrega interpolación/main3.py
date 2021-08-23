from lab3_cientifica import lagrange,newton, Householder, trozos, SepValues, plotpoly, newtferror,ftrerror,ferror,perror
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from time import time
import matplotlib.patches as mpatches

def main():

	t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7]
	y = [3624, 3644, 3666, 3658, 3653, 3640, 3669, 3703, 3694, 3739, 3731, 3752, 3739, 3773, 3803, 3786, 3788, 3767, 3782, 3778, 3763, 3777, 3796, 3803, 3799, 3795, 3805, 3848, 3859, 3888, 3881, 3850, 3837, 3767, 3741, 3691, 3696, 3723, 3717, 3773, 3739, 3716, 3726, 3723, 3704, 3720, 3729, 3739, 3802, 3841, 3875, 3908, 3893, 3887, 3896, 3907, 3858]
	
	'''
	t = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3]
	y = [31.0, 23.2, 22.4, 21.6, 20.8, 19.8, 19.8, 19.4, 19.1, 18.5, 18.1, 17.8, 17.6, 17.3, 17.2, 17.2, 18.4, 19.5, 21.7, 24.7, 26.5, 27.6, 28.0, 27.6, 26.3, 24.9, 22.9, 20.9, 19.9, 19.6, 19.0, 18.6, 18.3, 18.0, 17.7, 17.4, 17.1, 16.9, 16.7, 16.4, 17.6, 19.6, 21.6, 23.8, 25.9, 26.5, 26.8, 26.4, 25.6, 24.1, 21.9, 20.0, 19.0, 18.7, 18.5, 18.4, 18.1, 18.0, 17.6, 17.4, 17.6, 17.6, 17.4, 17.0, 18.0, 19.6, 21.2, 23.5, 25.5, 26.9, 26.6, 25.5, 23.7, 22.0, 20.8, 19.4, 18.7, 18.6, 18.1, 18.0, 18.1, 18.3, 17.9, 17.6]
	'''

	c,n = 10,len(t)-1
	tTrain,tVal, yTrain, yVal = SepValues(t,y,c) #Se separan los datos en validacion y entrenamiento
	tVal,yVal = tVal[0:len(tVal)-(n%c)],yVal[0:len(yVal)-(n%c)]	#se quitan los datos de validacion que esten por fuera de los de entrenamiento para evitar extrapolación
	x = np.linspace(t[0],tTrain[-1],1000)		
	print("Polinomial")
	HHStart = time()
	xHH,yHH,HHCoef = Householder(len(tTrain)-1,tTrain,yTrain)
	#Hallan elos errores absolutos error medio y desviacion estandar
	HHErr = ferror(HHCoef,tVal,yVal)
	HHmeanEr = np.mean(HHErr)
	HHStd = np.std(HHErr)
	perror(HHmeanEr,HHStd)
	HHTotal = time() - HHStart #Se evalua el timepo que tomo ejecutar el algoritmo de Transformaciones Householder
	print()
	print("A Trozos")
	AtStart = time()
	ansTr = trozos(tTrain,yTrain)
	AtErr = ftrerror(ansTr,tVal,yVal,c)	
	AtMean = np.mean(AtErr) 
	AtStd = np.std(AtErr)
	perror(AtMean,AtStd)
	AtTotal = time() - AtStart
	print()
	print("Lagrange")

	'''Lagrange'''	
	yn = 0
	LgStart= time()
	yn += lagrange(tTrain,yTrain,x) #polinomio para lagrange
	ynError = 0
	ynError += lagrange(tTrain,yTrain,tVal)
	errorAbs = abs((ynError - yVal)) #error absoluto para lagrange
	errorMedioAbs = stats.mean(errorAbs) #error medio para lagrange
	error_tipico = np.std(errorAbs) #error tipico para lagrange
	LgTotal= time() - LgStart
	perror(errorMedioAbs,error_tipico)
	print()
	print("Newton")

	NewtStart = time()
	yNewt,NewtCoef = newton(tTrain,yTrain,x)
	NewtErr = newtferror(tTrain,yVal,tVal,NewtCoef)	
	NewtmeanEr = np.mean(NewtErr)
	NewtStd = np.std(NewtErr)
	perror(NewtmeanEr,NewtStd)
	NewtTotal = time() - NewtStart
	print()
	print("Tiempos de Ejecución:")
	print("Polinomial: "+ str(HHTotal))
	print("A Trozos: "+ str(AtTotal))
	print("Newton: " + str(NewtTotal))
	print("Lagrange: " + str(LgTotal))
	plt.plot(tVal,yVal,'o', label = "Puntos de validacion")
	plt.plot(tTrain,yTrain,'o', label = "Puntos de entrenamiento")
	plt.plot(xHH,yHH, label = "Householder Transformations")
	plt.plot(x,yNewt,'y', label = "Newton")
	plt.plot(x, yn, 'b', label="Lagrange")
	plt.legend()
	plt.grid()
	plt.show()
main()
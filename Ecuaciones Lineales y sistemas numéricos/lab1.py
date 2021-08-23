import matplotlib.pyplot as plt

def numsys(b,t,L,U):
	"""
	Entrada: b el cual es un numero real referente al beta en el sistema (base), t
			hace las veces de la precision del sistema, por ultimo L y U son el rango 
			del exponente en el sistema, siendo L el más bajo y U el más alto 
	Salida: un sistema de punto flotante basado en los parametros que ingresaron en la funcion
			y una grafica que muestra la ubicacion del sistema en la recta
	Funcionamiento: El programa lo que realiza es un ciclo desde L hasta U en el que en cada iteracion
					se cuenta en binario, de acuerdo a la cantidad de posiciones en la mantisa
					(definido por t), por cada numero binario se guarda en el arreglo sistema
					el numero en punto flotante el cual está representando.
	"""
	ttemp = t-1
	maxi= pow(2,ttemp)-1 #Numero maximo de numeros binarios a representar con t-1 posiciones en la mantisa
	sistema = [0]
	while L<= U:
		i = 0
		while i <= maxi: 
			cont = bin(i)[2::] # tranformacion a binario
			if len(cont) != ttemp: 
				for _ in range(ttemp-len(cont)): #llenar las posiciones no utilizadas con 0´s
					cont = '0'+cont
			acum = 1
			for x in range(len(cont)):
				acum+= (int(cont[x])/pow(b,x+1)) #suma en la mantisa
			a = acum*(pow(b,L))
			sistema.append(a)
			sistema.append(-1*a)#agregar al sistema	el numero en punto flotante y su inverso aditivo		
			i+=1
		L+=1
	print(sistema)
	return sistema

def main():	
	b,t,L,U = 2,3,-1,1
	#b,t,L,U = 2, 5,-3,3
	#b,t,L,U = 2, 5,3,3
	ufl = pow(b,L)
	ofl = pow(b,U+1)*(1-pow(b,-t))
	n = (2*(b-1)*pow(b, t-1)*(U-L+1))+1
	print("n:",n)
	print("UFL:",ufl)
	print("OFL:",ofl)
	sistema = numsys(b,t,L,U)	
	plt.axhline(0,color = "black")
	y = [0 for _ in range(len(sistema))]
	plt.grid()
	plt.plot(sistema,y,'o', label = "Sistema Numerico")
	#plt.savefig("labTema1_3.png", bbox_inches='tight')
	plt.show()
	return
main()

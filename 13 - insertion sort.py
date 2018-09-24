def insertionsort(lista):
	for num in range(1, len(lista)):
		elemento = lista[num]
		cont = num - 1

		while cont >= 0 and lista[cont] > elemento:
			lista[cont + 1] = lista[cont]
			cont -= 1

		lista[cont + 1] = elemento

	print("Lista ordenada:", lista)
	return lista

lista = [7, 8, 5, 2, 4, 6, 3]
insertionsort(lista)
#Bubble sort com lista nativa de python ou vetor ---------
def bubblesort(lista, limite):
	if limite == 0 or limite == 1:
		print("Lista ordenada:", lista)
		return lista

	else:
		aux = 0
		for num in range(limite - 1):
			if lista[num] > lista[num + 1]:
				aux = lista[num]
				lista[num] = lista[num + 1]
				lista[num + 1] = aux

		bubblesort(lista, limite - 1)

lista = [5, 1, 4, 2, 8, 9]
bubblesort(lista, len(lista))
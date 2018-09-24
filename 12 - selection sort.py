#Selection sort com lista nativa de python ou vetor --------
def selectionsort(lista, inicio):
	if inicio + 1 == len(lista):
		print("Lista ordenada:", lista)
		return lista

	else:
		print(lista)
		posicao = inicio
		menor = lista[inicio]
		indice = inicio

		while indice < len(lista):
			if menor > lista[indice]:
				menor = lista[indice]
				posicao = indice

			indice += 1

		lista[posicao] = lista[inicio]
		lista[inicio] = menor
		selectionsort(lista, inicio + 1)

lista = [64, 25, 12, 22, 11]
selectionsort(lista, 0)		
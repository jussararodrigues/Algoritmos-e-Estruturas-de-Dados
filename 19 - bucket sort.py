def insertionsort(lista):
	for num in range(1, len(lista)):
		elemento = lista[num]
		cont = num - 1

		while cont >= 0 and lista[cont] > elemento:
			lista[cont + 1] = lista[cont]
			cont -= 1

		lista[cont + 1] = elemento

	return lista

def bucketsort(lista):
	size = max(lista)/len(lista)
	buckets = [[] for _ in range(len(lista))]
	
	for i in range(len(lista)):
		j = int(lista[i]/size)
		if j != len(lista):
			buckets[j].append(lista[i])
		else:
			buckets[len(lista) - 1].append(lista[i])
 
	for i in range(len(lista)):
		insertionsort(buckets[i])

	result = []

	for i in range(len(lista)):
 		result = result + buckets[i]

	print(result)
	return result

lista = [3,6,5,1,9,2,0]
bucketsort(lista)
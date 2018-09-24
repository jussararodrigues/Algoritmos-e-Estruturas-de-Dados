class Arvore():
	def __init__(self, chave, esq = None, dir = None):
		self.chave = chave
		self.esq = esq
		self.dir = dir

	#Insere uma nova chave na árvore ------------------------
	def inserir(self, no, chave):
		if no is None:
			no = Arvore(chave)
		
		elif chave < no.chave:
			if no.esq is None:
				no.esq = Arvore(chave)
			else:
				self.inserir(no.esq, chave)
		
		else:
			if no.dir is None:
				no.dir = Arvore(chave)
			else:
				self.inserir(no.dir, chave)

	#Busca uma chave na árvore ------------------------------
	def buscar(self, no, chave):
		if no is None:
			print(chave, "não foi encontrado na árvore.")
			return None
		
		elif no.chave == chave:
			return no
		
		elif chave > no.chave:
			return self.buscar(no.dir, chave)
		
		else:
			return self.buscar(no.esq, chave)

	#Exibe as chaves armazenadas na árvore -------------------
	def exibir(self, no):
		if no is None:
			return ""
		
		self.exibir(no.esq)
		print(no.chave, end=". ")
		self.exibir(no.dir)

	#Busca o pai de uma determinada chave da árvore ------------
	def buscarPai(self, no, chave):
		pai = no
		
		while no is not None:
			if no.chave == chave:
				return pai

			pai = no
			
			if no.chave < chave:
				no = no.dir
			else:
				no = no.esq
		
		return pai

	#Procura a chave mais a esquerda da subárvore da direita ---
	def maisEsq(self, no):
		no = no.dir

		while no.esq is not None:
			no = no.esq
		
		return no

	#Remove uma chave da árvore -------------------------------
	def remover(self, no, chave):
		#Verifica se a chave existe na árvore
		buscar = self.buscar(no, chave)

		if buscar is None:
			return ""

		#Busca o nó pai da chave que deseja-se remover
		pai = self.buscarPai(no, chave)

		#Remove o nó de chave sem filhos ou com apenas um filho
		if buscar.esq is None or buscar.dir is None:
			if buscar.esq is None:
				aux = buscar.dir
			else:
				aux = buscar.esq
			
			if chave > pai.chave:
				pai.dir = aux
			else:
				pai.esq = aux

		#Elimina o nó da chave que possui dois filhos
		else:
			mais = self.maisEsq(buscar)
			mais.esq = buscar.esq

			if pai.esq.chave == buscar.chave:
				pai.esq = mais
			else:
				pai.dir = mais


#Criando uma árvore
#O número passado como parâmetro é a raiz da árvore
arvore = Arvore(10)

arvore.inserir(arvore, 13)
arvore.inserir(arvore, 17)
arvore.inserir(arvore, 6)
arvore.inserir(arvore, 4)
arvore.inserir(arvore, 11)
arvore.inserir(arvore, 12)
arvore.inserir(arvore, 2)
arvore.inserir(arvore, 8)
arvore.inserir(arvore, 9)

'''
arvore.buscar(arvore, 2)
arvore.buscar(arvore, 5)
arvore.buscar(arvore, 8)
arvore.buscar(arvore, 7)
'''

arvore.exibir(arvore)

arvore.remover(arvore, 6)

print()
arvore.exibir(arvore)
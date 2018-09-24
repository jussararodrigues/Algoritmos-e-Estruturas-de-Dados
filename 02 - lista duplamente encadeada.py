class No():
	def __init__(self, item = None, ant = None, prox = None):
		self.item = item
		self.ant = ant
		self.prox = prox

	'''def getItem(self):
		return self.__item
	def setItem(self, item):
		self.__item = item

	def getAnt(self):
		return self.__ant
	def setAnt(self, ant):
		self.__ant = ant

	def getProx(self):
		return self.__prox
	def setItem(self, prox):
		self.__prox = prox'''

class Lista():
	def __init__(self, primeiro = None, ultimo = None):
		self.__primeiro = primeiro
		self.__ultimo = self.__primeiro

	def inserirFim(self, item):
		novoNo = No(item)

		if self.__primeiro is None:
			self.__primeiro = novoNo
			self.__ultimo = self.__primeiro

		else:
			novoNo.ant = self.__ultimo
			self.__ultimo.prox = novoNo
			self.__ultimo = novoNo

		print(novoNo.item, "inserido!")

	def inserirInicio(self, item):
		novoNo = No(item)

		if self.__primeiro is None:
			self.__primeiro = novoNo
			self.__ultimo = self.__primeiro

		else:
			novoNo.prox = self.__primeiro
			self.__primeiro = novoNo

	def removerItem(self, item):
		noAtual = self.__primeiro

		while noAtual is not None:
			if noAtual.item == item:
				if noAtual.ant is None:
					self.__primeiro = noAtual.prox
					noAtual.prox.ant = None
				else:
					noAtual.prox.ant = noAtual.ant
					noAtual.ant.prox = noAtual.prox

				exc = noAtual
				noAtual = None
				del exc

			else:
				noAtual = noAtual.prox

	def removerFim(self):
		if self.__primeiro is not None:
			aux = self.__ultimo
			self.__ultimo = self.__ultimo.ant
			self.__ultimo.prox = None
			del aux
		else:
			return "Lista vazia."

	def removerInicio(self):
		if self.__primeiro is not None:
			aux = self.__primeiro
			self.__primeiro = self.__primeiro.prox
			self.__primeiro.ant = None
			del aux
		else:
			return "Lista vazia."

	def procurar(self, item):
		noAtual = self.__primeiro

		while noAtual is not None and noAtual.item != item:
			noAtual = noAtual.prox
	
		if noAtual is None:
			print("Não encontrado :(")
		else:
			print("Encontrado!")

	def exibir(self):
		noAtual = self.__primeiro

		while noAtual is not None:
			print(noAtual.item)
			noAtual = noAtual.prox

lista = Lista()
lista.inserirFim(3)
lista.inserirFim(4)
lista.inserirFim(5)

lista.procurar(5)
lista.exibir()
lista.removerItem(4)
lista.removerItem(3)
lista.removerItem(5)
lista.exibir()
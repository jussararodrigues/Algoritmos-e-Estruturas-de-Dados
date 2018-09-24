class No():
	def __init__(self, item = None, ant = None, prox = None):
		self.item = item
		self.ant = ant
		self.prox = prox

#PILHA ------------------------------------------------------------------
class Pilha():
	def __init__(self, primeiro = None, ultimo = None):
		self.primeiro = primeiro
		self.ultimo = self.primeiro

	def adicionar(self, item):
		novoNo = No(item)

		if self.primeiro is None:
			self.primeiro = novoNo
			self.ultimo = self.primeiro

		else:
			self.ultimo.prox = novoNo
			novoNo.ant = self.ultimo
			self.ultimo = novoNo

	def remover(self):
		aux = self.ultimo
		self.ultimo.ant.prox = None
		self.ultimo = self.ultimo.ant

		del aux

	def exibir(self):
		noAtual = self.primeiro
		print("-- PILHA --")

		while noAtual is not None:
			print("|", noAtual.item, "|")
			noAtual = noAtual.prox

		print()

pilha = Pilha()
pilha.adicionar(8)
pilha.adicionar(2)
pilha.adicionar(5)
pilha.adicionar(0)
pilha.exibir()
pilha.remover()
pilha.exibir()

#-----------------------------------------------------------------------

#FILA ------------------------------------------------------------------
class Fila():
	def __init__(self, primeiro = None, ultimo = None):
		self.primeiro = primeiro
		self.ultimo = self.primeiro

	def adicionar(self, item):
		novoNo = No(item)

		if self.primeiro is None:
			self.primeiro = novoNo
			self.ultimo = self.primeiro

		else:
			self.ultimo.prox = novoNo
			novoNo.ant = self.ultimo
			self.ultimo = novoNo

	def remover(self):
		aux = self.primeiro
		self.primeiro.prox.ant = None
		self.primeiro = self.primeiro.prox

		del aux

	def exibir(self):
		noAtual = self.primeiro
		print("-- FILA --")

		while noAtual is not None:
			print("|", noAtual.item, "|")
			noAtual = noAtual.prox

		print()

fila = Fila()
fila.adicionar(6)
fila.adicionar(0)
fila.adicionar(1)
fila.adicionar(9)
fila.exibir()
fila.remover()
fila.exibir()
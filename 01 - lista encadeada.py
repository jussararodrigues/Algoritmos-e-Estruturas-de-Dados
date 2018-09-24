class No():
	def __init__(self, item, prox = None):
		self.item = item
		self.prox = prox

class Lista():
	def __init__(self, primeiro = None, ultimo = None):
		self.primeiro = primeiro
		self.ultimo = self.primeiro

	def inserirFim(self, item):
		novoNo = No(item)
		
		if self.primeiro is None:
			self.primeiro = novoNo
			self.ultimo = self.primeiro

		else:
			noAtual = self.primeiro
			while noAtual.prox is not None:
				noAtual = noAtual.prox

			noAtual.prox = novoNo
			self.ultimo = novoNo

	def inserirInicio(self, item):
		novoNo = No(item)
		if self.primeiro is None:
		 	self.primeiro = novoNo
		 	self.ultimo = self.primeiro

		else:
		 	novoNo.prox = self.primeiro
		 	self.primeiro = novoNo

	def buscar(self, item):
		noAtual = self.primeiro

		while noAtual is not None:
			if noAtual.item == item:
				print("")
				print(item, "encontrado!!!")
				return ""
			else:
				noAtual = noAtual.prox

		print("")
		print(item, "não encontrado :(")

	def removerInicio(self):
		exc = self.primeiro
		self.primeiro = self.primeiro.prox
		print(exc.item, "removido.")
		del exc

	def removerFim(self):
		noAtual = self.primeiro

		while noAtual.prox.prox is not None:
			noAtual = noAtual.prox

		exc = noAtual.prox
		noAtual.prox = None
		self.ultimo = noAtual
		print(exc.item, "removido.")
		del exc

	def removerItem(self, item):
		noAtual = self.primeiro

		while noAtual.prox is not None:
			if noAtual.item != item:
				if noAtual.prox.item == item:
					exc = noAtual.prox
					noAtual.prox = noAtual.prox.prox
					if noAtual.prox is self.ultimo:
						self.ultimo = noAtual

					print(exc.item, "removido.")
					del exc
					return ""
				else:
					noAtual = noAtual.prox
			else:
				exc = noAtual
				self.primeiro = self.primeiro.prox
				print(exc.item, "removido.")
				del exc
				return ""

		print(item, "não encontrado :(")

	def exibir(self):
		noAtual = self.primeiro
		lista = ""

		while noAtual is not None:
			lista += "|" + str(noAtual.item) + "| "
			noAtual = noAtual.prox

		print(lista)

lista = Lista()
lista.inserirFim(7)
lista.inserirFim(9)
lista.inserirFim(5)
lista.inserirFim(2)

lista.exibir()

lista.removerFim()

lista.exibir()
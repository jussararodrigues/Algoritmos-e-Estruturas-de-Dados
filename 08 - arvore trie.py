class No():
	def __init__(self, cpf = None, pessoa = None, fim = False):
		self.cpf = cpf
		self.pessoa = pessoa
		self.fim = False
		self.chaves = [None] * 10

class BancoDeDados():
	def __init__(self):
		self.raiz = No()

	def adicionar(self, cpf, pessoa):
		no = self.raiz
		cpf = str(cpf)

		for num in cpf:
			if no.chaves[int(num)] is None:
				no.chaves[int(num)] = No(int(num))
				no = no.chaves[int(num)]
			else:
				no = no.chaves[int(num)]

		no.fim = True
		no.pessoa = pessoa
		print(cpf, "Adicionado.\n")

	def buscar(self, cpf):
		no = self.raiz
		cpf = str(cpf)

		for num in cpf:
			if no.chaves[int(num)] is not None:
				no = no.chaves[int(num)]
			else:
				print("CPF", cpf, "não cadastrado.\n")
				return None

		if no.fim is True:
			print("-" * 35)
			print("CPF:", cpf)
			print("Portador(a) do CPF:", no.pessoa)
			print("-" * 35)
			return no
		else:
			print("CPF", cpf, "não cadastrado.\n")

	'''
	def remover(self, cpf):
		buscar = self.buscar(cpf)

		if buscar is not None:
			no = self.raiz
			cpf = str(cpf)

			for num in cpf:
				no = no.chaves[int(num)]

		else:
			print("CPF", cpf, "não cadastrado.")
	'''

bd = BancoDeDados()
bd.adicionar(703, "Jussara")
bd.adicionar(702, "Jéssica")
bd.adicionar(700, "Mariana")
bd.adicionar(100, "Moisés Júnior")
bd.buscar(702)
bd.buscar(100)
bd.buscar(102)
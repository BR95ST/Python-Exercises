class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	

	def getNome(self):
		return self.nome

	def getIdade(self):
		return self.idade

	def setNome(self, nome):
		 self.nome = nome

	def setIdade(self, idade):
		self.idade = idade
 
p1 = Pessoa('Bruno', 23)
p2 = Pessoa('Donnie', 17)
p3 = Pessoa('Splenger', 35)

pessoas = []

pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)

for pessoa in pessoas:
	print(pessoa.getNome())
	

"""
print('Nome: %s'%p1.getNome())
print('Idade: %d'%p1.getIdade())
"""

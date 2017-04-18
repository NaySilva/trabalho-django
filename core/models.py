from django.db import models

# Create your models here.
class Contato(models.Model):
	nome = models.CharField(max_length=20)
	endereco = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length=20)

	def __str__(self):
		return self.nome

class Cliente(models.Model):
	cpf = models.CharField(max_length=14)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=8)
	foneResidencial = models.CharField(max_length=15)
	foneTrabalho = models.CharField(max_length=15)
	rendaFamiliar = models.DecimalField(max_digits=10, decimal_places=2)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Venda(models.Model):
	dataVenda = models.DateField()
	valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
	cliente = models.ForeignKey(Cliente)

	def __str__(self):
		return '%s - %d' % (self.cliente.nome, self.valorTotal)

class Produto(models.Model):
	nomeProduto = models.CharField(max_length=35)
	quantidade = models.IntegerField()
	minQuantidade = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.nomeProduto

class ItemVenda(models.Model):
	venda = models.ForeignKey(Venda)
	produto = models.ForeignKey(Produto)
	precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField()

	def __str__(self):
		return '%s - %s' % (self.venda.__str__, self.produto.__str__)

class Fornecedor(models.Model):
	cnpj = models.CharField(max_length=20)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=8)
	fone = models.CharField(max_length=15)
	responsavel = models.CharField(max_length=30)
	website = models.CharField(max_length=80)

	def __str__(self):
		return self.nome

class Pedido(models.Model):
	dataPedido = models.DateField()
	dataRecebimento = models.DateField()
	precoTotal = models.DecimalField(max_digits=10, decimal_places=2)
	fornecedor = models.ForeignKey(Fornecedor)

	def __str__(self):
		return '%s - %d' % (self.fornecedor.nome, self.precoTotal)

class ItemPedido(models.Model):
	pedido = models.ForeignKey(Pedido)
	produto = models.ForeignKey(Produto)
	precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField()

	def __str__(self):
		return '%s - %s' % (self.pedido.__str__, self.produto.__str__)





from django.contrib import admin
from .models import *

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone')

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cpf', 'nome', 'endereco', 'complemento', 'cidade', 'estado', 'cep', 'foneResidencial', 'foneTrabalho', 'rendaFamiliar', 'email')

class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('cnpj', 'nome', 'endereco', 'complemento', 'cidade', 'estado', 'cep', 'fone', 'responsavel', 'website')

class VendaAdmin(admin.ModelAdmin):
	list_display = ('dataVenda', 'valorTotal', 'cliente')

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nomeProduto', 'quantidade', 'minQuantidade')

class ItemVendaAdmin(admin.ModelAdmin):
	list_display = ('venda', 'produto', 'precoUnitario', 'quantidade')

class ItemPedidoAdmin(admin.ModelAdmin):
	list_display = ('pedido', 'produto', 'precoUnitario', 'quantidade')

class PedidoAdmin(admin.ModelAdmin):
	list_display = ('dataPedido', 'dataRecebimento', 'precoTotal', 'fornecedor')

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ItemVenda, ItemVendaAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
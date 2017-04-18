from django.utils import timezone
import datetime

date = timezone.now()
# 2.a
cliente = Cliente(1, '12345','Maria','Rua 1', 'praça', 'Teresina', 'PI', '64000-000', '86 3222-2222', '86 3122-2222', 2000.00, 'maria@gmail.com')
cliente.save()

# 2.b
fornecedor = Fornecedor(1, '12346','João','Rua 11', 'praça', 'Teresina', 'PI', '64000-000', '86 3322-2222', 'Seu Ze','fornecedor.com')
fornecedor.save()
# 2.f
venda = Venda(1, date, 500.00, 1)
venda.save()

# 2.c
produto = Produto(1,'produto1', 20, 50)
produto.save()

# 2.g
itemVenda = ItemVenda(1,1,1,50.0,10)
itemVenda.save()

# 2.e
itemPedido = ItemPedido(1,1,1,100.00, 5)
itemPedido.save()

# 2.d
pedido = Pedido(1,date,date+datetime.timedelta(days=1),500.00,1)
pedido.save()

# 3.a
Cliente.objects.all()

# 3.b
Venda.objects.filter(cliente=1)

# 3.c
Pedido.objects.get(pk=1)

# 3.d
ItemPedido.objects.filter(pedido=1)

# 3.e
from django.db.utils import F
Produto.objects.filter(quantidade=F('minQuantidade'))
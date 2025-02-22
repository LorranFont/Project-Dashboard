from rest_framework import viewsets
from .models import Produto, Venda, Estoque, Usuario, Oferta
from .serializers import ProdutoSerializer, VendaSerializer, EstoqueSerializer, UsuarioSerializer, OfertaSerializer

# ViewSet para Produtos
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# ViewSet para Vendas
class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

# ViewSet para Estoque
class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

# ViewSet para Usuários
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# ViewSet para Ofertas
class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, VendaViewSet, EstoqueViewSet, UsuarioViewSet, OfertaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'ofertas', OfertaViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]

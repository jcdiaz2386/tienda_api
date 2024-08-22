from django.urls import path
from .views import ProductoListCreate
from .views import ProductoListCreate, lista_productos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('lista/', lista_productos, name='lista-productos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

from product.views.product_view import index_view

urlpatterns = [
    path('', index_view, name='index'), #raiz del proyecto
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")), #la ruta q empiexe con products, trae todas
    #las rutas de urls products
]
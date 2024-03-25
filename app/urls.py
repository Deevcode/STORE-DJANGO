from django.urls import path
from .views import home, tienda, contacto

urlpatterns = [
    path('', home, name="home"),
    path('tienda/', tienda, name="tienda"),
    path('contacto/', contacto, name="contacto"),
]

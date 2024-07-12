from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('instagram/', views.ig_view, name='ig'),
    path('', RedirectView.as_view(url='index/', permanent=False)),  # Redirige a index/
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('registrate/', views.registrate, name='registrate'),  # Añadir vista de registro
    path('agregar/', views.agregar, name='agregar'),  # Para agregar vehículos
    path('modificar/<int:pk>/', views.encontrar, name='modificar'),  # Modificar vehículo
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),  # Eliminar vehículo
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
